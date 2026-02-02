CREATE OR REPLACE PROCEDURE HR_DB.HR_SCHEMA.STAGE_TO_PROD_TABLE_SP()
RETURNS TABLE()
LANGUAGE PYTHON
RUNTIME_VERSION = '3.9'
PACKAGES = ('snowflake-snowpark-python')
HANDLER = 'main'
COMMENT = 'SNOWFLAKE AS SANDBOX FOR SNOWPARK PYTHON PROGRAM'
EXECUTE AS OWNER
AS
$$
import snowflake.snowpark as snowpark
from snowflake.snowpark.types import StructType, StructField, StringType, IntegerType, DoubleType,BooleanType
from snowflake.snowpark.functions import col

def main(session:snowpark.Session):
    schema = StructType([ 
    StructField("name", StringType()),
    StructField("gender", StringType()),
    StructField("age", IntegerType()),
    StructField("class", StringType()), 
    StructField("embarked", StringType()),
    StructField("country", StringType()),
    StructField("ticketno", IntegerType()),
    StructField("fare", DoubleType()),
    StructField("sibsp", IntegerType()),
    StructField("parch", IntegerType()),
    StructField("survived",BooleanType())  
    ])
    titanic_df = session.read.schema(schema).options({"field_delimiter":",","skip_header":1,"field_optionally_enclosed_by":"\042",'null_if':'NA'}).csv("@hr_db.hr_schema.TITANIC_STG/")    
    count_before = titanic_df.count()

    #apply 2 filters on titanic data frame
    titanic_df = titanic_df.filter(col("GENDER")=='male').where(col("EMBARKED")=='S')
    titanic_df.show()

    count_after = titanic_df.count()

    #sort my datafrmat by using pclass
    titanic_df = titanic_df.order_by(col("CLASS"))

    #print the count and write into the table
    cnt_msg = "<custom msg> titanic ship passenger counts before " + str(count_before) + "& After:= " + str(count_after)
    
    print(cnt_msg)

    ## write data into the titanic table
    
    titanic_df.write.save_as_table("HR_DB.HR_SCHEMA.TITANIC_PASSENGER_TBL",mode="ignore",table_type="transient")


    return titanic_df
    $$
;
call HR_DB.HR_SCHEMA.STAGE_TO_PROD_TABLE_SP();


call HR_DB.HR_SCHEMA.NEW_PYTHON_SP()