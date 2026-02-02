'''
1) to date() 
     - Convert Timestamp to Datejusing snowpark
2) date_format () 
     - Convert Date to String format with snowpark
3) Difference between two dates (days, months, years) with snowpark

'''

import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col,to_date,lit,to_timestamp
from snowflake.snowpark.types import StructField,StructType,StringType,IntegerType,LongType
import logging
import sys

logging.basicConfig(filename=r'H:\cloudfire_snowpark\workspace_snowpark_python\snowpark_datafrmaes\na_log.log',
                    level = logging.INFO,
                    format = '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt = '%I:%M:%S'
                    )

connection_params = {
    "account":"ETADEVCQX-YODSTES01921",
    "user":"ventgdg@136",
    "password":"Venkata@@$sg12456",
    "roles":"ACCOUNTADMIN",
    "warehouse":"COMPUTE_WH",
    "database":"HR_DB",
    "schema":"HR_SCHEMA"
}

new_session = Session.builder.app_name('timestamp_date').configs(connection_params).getOrCreate()

data = [ ("1", "2019-06-24 12:01:19.000") ]
schema=["id", "input_timestamp"]

# data = [("1", "2019-07-01") , ("2", "2019-06-24"), ("3", "2019-08-24") ]

# data = [("1", "2019-07-01") , ("2", "2019-06-24") , ("3", "2019-08-24") ]

df = new_session.createDataFrame(data,schema)
# df.show()

df=df.withColumn('date_type',to_date(col('INPUT_TIMESTAMP')))

# df.printSchema()

df.select(to_date(lit('2019-06-24 12:01:19.000')).alias("date")).show()

df1=df.select(to_timestamp(lit('2019-06-24 12:01:19.000')).alias("timestamp"))

# df1.show()

#casting

df2 = df.withColumn('date_type',to_timestamp(col('INPUT_TIMESTAMP')).cast('date'))
df2.printSchema()
df2.show()

df3 = new_session.sql('select to_date(current_timestamp) as date')
df3.show()
df3.printSchema()

df4 = new_session.sql("select to_timestamp('06-24-2020 12:01:19.718','MM-dd-yyyy HH:mm:ss.FF3') as time")
df4.show()
df4.print_schema()