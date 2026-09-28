from pyspark.sql import SparkSession
from validate import validate_data
from transform import transform_data
from load import laod_data

spark = SparkSession.builder.appName("Retail ETL").getOrCreate()

print("ETL py started")
validate_data(spark)
transform_data(spark)
laod_data(spark)

spark.stop()