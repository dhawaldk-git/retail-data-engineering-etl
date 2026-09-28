from extract import read_data
import logging

logging.basicConfig(
    filename="../logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s - %(message)s"
)

logging.info("Validation Started")

def validate_data(spark):
    orders_df, customers_df, products_df = read_data(spark)

    orders_df.printSchema()

    logging.info(f"total record: {orders_df.count()}")

    total = orders_df.count()
    unique = orders_df.dropDuplicates().count()
    print(f"Duplicates = {total - unique}")

    print("Invalid Quantity")
    orders_df.filter("quantity <= 0").show()
    logging.info("Validation Completed")
# spark.stop()