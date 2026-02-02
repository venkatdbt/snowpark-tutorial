'''A Permanent UDF registers functions as UDFs in the Snowflake database. When you create a permanent
UDF, it is mandatory to set the is_permanent argument to True and the stage_location argument to the
stage location where the & Python file for the UDF and its dependencies are uploaded.

A Permanent UDF can be created in Snowpark using any of the beow methods.

1). The udf function, in the snowflake.snowpark.functions module, with the name argument.
2). The register method, in the UDFRegistration class, with the name argument.

'''

import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import udf,col,lit
from snowflake.snowpark.types import IntegerType,StringType,FloatType
import re

connection_params = {
    "account":"ETADEVCQX-YODSTES01921",
    "user":"ventgdg@136",
    "password":"Venkata@@$sg12456",
    "roles":"ACCOUNTADMIN",
    "warehouse":"COMPUTE_WH",
    "database":"HR_DB",
    "schema":"HR_SCHEMA"
}



new_session = Session.builder.app_name('permanent_udf_2023').configs(connection_params).getOrCreate()

@udf(name='cal_bonus',return_type=IntegerType(),input_types=[IntegerType(),IntegerType()],is_permanent=True,replace=True,stage_location='@SNOWPARK_UDF')
def calculate_bonus(salary:int,rating:int)->int:
    #Define bonus Calculation logic
    base_bonus = 0.1 * salary    ## 10% of salary
    rating_bonus = 0.05 * salary * (rating - 3)
    total_bonus = base_bonus + rating_bonus
    return total_bonus 

emp_data = [(1,50000,4),(2,60000,5),(3,45000,3),(4,70000,4)]

schema = ["employee_id","salary","rating"]

df = new_session.createDataFrame(data=emp_data,schema=schema)

df.createOrReplaceTempView('emp_info')
new_session.sql(" SELECT *,cal_bonus(SALARY,RATING) as total_sal FROM EMP_INFO ").show()

emp_df = new_session.table('HR_DB.HR_SCHEMA.EMPLOYEES')

emp_df.select(col('EMPLOYEE_ID'),col('SALARY'),lit(5).as_('RATING'),
              calculate_bonus(col('SALARY'),col('RATING')).alias('TOTAL_SAL')).show()