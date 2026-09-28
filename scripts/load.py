# from pyspark.sql import SparkSession

# spark = SparkSession.builder.appName("Load").getOrCreate()

def laod_data(spark):
    print("load Started")
    df = spark.read.csv("../output/ranked_customers.csv",
                        header=True,
                        inferSchema=True)

    df.show()