from pyspark.sql.functions import col,sum,desc,row_number,broadcast
from pyspark.sql.window import Window
from extract import read_data
import logging

logging.basicConfig(
    filename="../logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s - %(message)s"
)

def transform_data(spark):
    print("Transform py Started")
    logging.info("Transform Started")
    orders_df, customers_df, products_df = read_data(spark)

    # final_df = orders_df.join(customers_df,'customer_id').join(products_df,'product_id')
    final_df_brod = (orders_df.join(broadcast(customers_df),'customer_id').join(broadcast(products_df),'product_id'))

    # print(final_df.columns)
    final_df = final_df_brod.withColumn("revenue", col('quantity') * col('price'))
    print("Final DF")
    final_df.show()
    final_df.select(sum('revenue')).show()

    category_sales = final_df.groupBy('category').agg(sum('revenue').alias('total_revenue'))
    print("category sales")
    category_sales.show()

    top_customer = final_df.groupBy('customer_name').agg(sum('revenue').alias('total_spent')).orderBy(desc('total_spent'))
    print("Tp Customer by revenue")
    top_customer.show()

    # top_customer.filter(col('total_spent') > 1000).show()

    window_spec = Window.orderBy(col('total_spent').desc())

    rank_customers = top_customer.withColumn('rank',row_number().over(window_spec))
    # rank_customers.show()
    # pdf = rank_customers.toPandas()
    # pdf.to_csv("../output/ranked_customers.csv",
    # index=False)
    # print("CSV Written Successfully")

    logging.info("Transform Completed Successfully")
    print("Transform Stop")

    return rank_customers

# spark.stop()