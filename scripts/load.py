# from pyspark.sql import SparkSession
from sql.create_database import get_database

# spark = SparkSession.builder.appName("Load").getOrCreate()

def laod_data(df):
    print("load Started")
    engine = get_database()
    # df = spark.read.csv("../output/ranked_customers.csv",
    #                     header=True,
    #                     inferSchema=True)
    
    pdf = df.toPandas()
    pdf.to_sql(
    "ranked_customers",
    engine,
    if_exists="replace",
    index=False
    )
    print("Load Complete")