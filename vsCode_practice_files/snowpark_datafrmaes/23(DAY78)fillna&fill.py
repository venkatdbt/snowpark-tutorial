import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import max,min,avg,mean,col
from snowflake.snowpark.types import StructField,StructType,StringType,IntegerType,LongType
import logging
import sys

connection_params = {
    "account":"ETADEVCQX-YODSTES01921",
    "user":"ventgdg@136",
    "password":"Venkata@@$sg12456",
    "roles":"ACCOUNTADMIN",
    "warehouse":"COMPUTE_WH",
    "database":"HR_DB",
    "schema":"HR_SCHEMA"
}

logging.basicConfig(filename=r'H:\cloudfire_snowpark\workspace_snowpark_python\snowpark_datafrmaes\na_log.log',
                    level = logging.INFO,
                    format = '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt = '%I:%M:%S'
                    )

custom_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("zipcode", LongType(), True),
    StructField("type", StringType(), True),
    StructField("city", StringType(), True),
    StructField("state", StringType(), True),
    StructField("population", LongType(), True)
])


def main() -> None:
     new_session = Session.builder.app_name("fill_na").configs(connection_params).getOrCreate()
    
     df = new_session.read \
        .schema(custom_schema) \
        .options({"field_delimiter": ",","skip_header": 1,'compression':'None'}) \
        .csv('@"HR_DB"."HR_SCHEMA"."FILL_NA_STAGE"/na/stg/small_zipcode.csv')
     print(df.columns)
     logging.info('columns are {}'.format(df.columns))
    #  df.show()
    #  df.fillna(value=0).show() #replace nulls with zero
    #  df.na.fill(value=0).show()
    #  df.fillna(value='unknown',subset=['TYPE','CITY']).show()
    #  df.na.fill(value=0,subset=['POPULATION','TYPE']).show() #type is string type so we cant replace with zero
    #  df.fillna(value='unknown',subset=['CITY']).fillna(value="",subset=['TYPE']).show()
     df.na.fill({'CITY':'UNKNOWN','TYPE':'NULL_1'}).show()
     df1=df.fillna({'CITY':'UNKNOWN','TYPE':'NULL_1'})

     df1.write.mode('overwrite').parquet('@"HR_DB"."HR_SCHEMA"."FILL_NA_STAGE"/na/stg/')
     
     logging.info('file is successfully written in to the external stage')
     return None

if __name__=='__main__':
     main()