import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.types import StructField,StructType,StringType,LongType,IntegerType,DoubleType,BooleanType
from snowflake.snowpark.functions import col
import logging
import os
import sys

#initiate logging at INFO level
logging.basicConfig(stream=sys.stdout,level=logging.DEBUG,format='%(levelname)s - %(message)s')

#initiate the snowpark session
def get_snowpark_session()->Session:
    connection_params = {
     "account":"ETADEVCQX-YODSTES01921",
     "user":"ventgdg@136",
     "password":"Venkata@@$sg12456",
     "roles":"ACCOUNTADMIN",
     "warehouse":"COMPUTE_WH",
     "database":"HR_DB",
     "schema":"HR_SCHEMA"
    }
    session = Session.builder.app_name("deploy snowpark in local sandbox").configs(connection_params).create()
    return session


def main():
    logging.info("starting the main methods ....<custome message>")

    session = get_snowpark_session()

#### Change the context(role,schema,database,wh)

    session.sql("use role ACCOUNTADMIN").collect()
    session.sql("use database HR_DB").collect()
    session.sql("use schema HR_DB.HR_SCHEMA").collect()
    session.sql("use warehouse COMPUTE_WH").collect()
    logging.info("<custom msg> set the context level")
    
######### Delele the table if exists in the snowflake environment
    
    session.sql("drop table if exists HR_DB.HR_SCHEMA.TITANIC_PASSENGER_TBL").collect()
    logging.info("<custom-msg> drop the the table if exists")

######### read the datafile form the internal stage
    schema = StructType([
    # StructField("name1", StringType()),  
    StructField("name", StringType()),
    StructField("gender", StringType()),
    StructField("age", IntegerType()),
    StructField("class", StringType()),  # Assuming class is a numeric value
    StructField("embarked", StringType()),
    StructField("country", StringType()),
    StructField("ticketno", IntegerType()),
    StructField("fare", DoubleType()),
    StructField("sibsp", IntegerType()),
    StructField("parch", IntegerType()),
    StructField("survived",BooleanType())  # Assuming survived is a binary indicator (0 or 1)
    ])
    titanic_df = session.read.schema(schema).options({"field_delimiter":",","skip_header":1,"field_optionally_enclosed_by":"\042",'null_if':'NA'}).csv("@hr_db.hr_schema.TITANIC_STG/")
    
    print(titanic_df.collect()[:5])
    # titanic_df.show()
    ### check count
    count_before = titanic_df.count()

    #apply 2 filters on titanic data frame
    titanic_df = titanic_df.filter(col('"GENDER"')=='male').where(col('"EMBARKED"')=='S')
    titanic_df.show()

    count_after = titanic_df.count()

    #sort my datafrmat by using pclass
    titanic_df = titanic_df.order_by(col('"CLASS"'))

    # print the count and write into the table
    cnt_msg = "<custom msg> titanic ship passenger counts before " + str(count_before) + "& After:= " + str(count_after)
    
    # logging.info(cnt_msg)
    print(cnt_msg)

    ## write data into the titanic table
    
    titanic_df.write.save_as_table("HR_DB.HR_SCHEMA.TITANIC_PASSENGER_TBL",mode="overwrite",table_type="transient")
    logging.info("<custom msg> created a trnasient table and publish the result")
    
if __name__ == "__main__":
    main()

