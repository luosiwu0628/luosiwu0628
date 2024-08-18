import pandas as pd
# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 27, 22]}
df = pd.DataFrame(data)

# Print DataFrame
print(df)
from pyspark.sql import SparkSession
# Initialize a Spark session
spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()

# Optionally, verify the Spark session is created
print(spark)
# List all available tables
tables = spark.catalog.listTables()
for table in tables:
    print(table.name)