import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
import logging
import sys



logging.basicConfig(filename=r'H:\cloudfire_snowpark\workspace_snowpark_python\snowpark_datafrmaes\pivot.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%I:%M:%S' 
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

new_session = Session.builder.app_name('pivot_agg').configs(connection_params).getOrCreate()

data = [("Banana",1000,"USA"), ("Carrots",1500,"USA"), ("Beans",1600,"USA"), \
("Orange",2000,"USA"),("Orange",2000,"USA"),("Banana",400,"China"), \
("Carrots",1200,"China"),("Beans",1500,"China"),("Orange",4000,"China"),\
("Banana",2000,"Canada"), ("Carrots",2000,"Canada"),("Beans",2000,"Mexico")] 

columns= ["Product","Amount","Country"]

logging.info('The columns ::: '+str(columns))

df = new_session.createDataFrame(data=data,schema=columns)
df.show()

pivot_df = df.groupBy(col('PRODUCT')).pivot(col('COUNTRY')).sum(col('AMOUNT'))

pivot_df.printSchema()

print(pivot_df.collect()[2])

print(pivot_df.collect()[2][2])

pivot_df.show()

logging.info('banana in china is {}'.format(pivot_df.collect()[3][2]))

pivot_df.write.mode('append').csv('@SNOWPARK_UDF',header=True,partition_by=col('PRODUCT'))
