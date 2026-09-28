
# print("Extract Started")
def read_data(spark):
    
    orders_df = spark.read.csv(
        "../data/orders.csv",
        header=True,
        inferSchema=True
    )

    customers_df = spark.read.csv(
        "../data/customers.csv",
        header=True,
        inferSchema=True
    )

    products_df = spark.read.csv(
        "../data/products.csv",
        header=True,
        inferSchema=True
    )

    return orders_df,customers_df,products_df
# print("Orders")
# orders_df.show()

# print("Customers")
# customers_df.show()

# print("Products")
# products_df.show()
# print("Extract Stop")
