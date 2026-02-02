'''
The register_from_file method, in the UDFRegistration class, registers a º Python function from a R
Python or zip file as a Snowflake Python UDF. Apart from file_path and func_name, the input
arguments of this method are the same as the register method.

'''
import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from snowflake.snowpark.types import IntegerType,StringType
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


new_session = Session.builder.app_name('UDF_FROM_FILE').configs(connection_params).getOrCreate()

udf_cal_bonus = new_session.udf.register_from_file(
file_path = r"H:\cloudfire_snowpark\workspace_snowpark_python\snowpark_datafrmaes\18_1_1L1_tx.py",
func_name = 'calculate_bonus',
return_type=IntegerType(),
input_types = [IntegerType()]
)

df = new_session.table('HR_DB.HR_SCHEMA.EMPLOYEES')

# df.show()

df1 = df.select(col('EMPLOYEE_ID'),col('SALARY'),udf_cal_bonus(col('SALARY')).as_('BONUS'))
df1.show()