'''
A Permanent UDF can be registered in Snowflake using a Python file from your local development
environment. Initially, the file should be imported to an Internal Stage, and then, using the
register_from_file method, the function defined in the & Python file can be registered as Snowflake R
Python UDF.

'''

import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from snowflake.snowpark.types import IntegerType,StringType,ArrayType,StructType,StructField
from snowflake.snowpark import PutResult #return result of put file from local to stage
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

new_session.file.put(local_file_name=r'H:\cloudfire_snowpark\workspace_snowpark_python\snowpark_datafrmaes\18_3_L3_tx.py',
                     stage_location='@SNOWPARK_UDF'
                    )
[PutResult(source='18_3_L3_tx.py'
                                ,target='18_3_L3_tx.py'
                                ,source_size=100
                                ,target_size=200
                                ,source_compression='NONE'
                                ,target_compression='NONE'
                                ,status='uploaded'
                                ,message='18_3_L3_tx.py file is successfully uploaded')]

udf_evenodd = new_session.udf.register_from_file(
    file_path = '@SNOWPARK_UDF/18_3_L3_tx.py',
    func_name='ODD_EVEN',
    input_types =  [IntegerType()],
    return_type = StringType()
)


udf_filter_emp_salary = new_session.udf.register_from_file(
    file_path = '@SNOWPARK_UDF/18_3_L3_tx.py',
    func_name = 'filter_emp_salary',
    input_types =  [IntegerType()],
    return_type = ArrayType()
)

df = new_session.table('HR_DB.HR_SCHEMA.EMPLOYEES')


df.show()

df1 = df.select(col('EMPLOYEE_ID'),udf_evenodd(col('EMPLOYEE_ID')).alias('emp_id_odd_even'))

df1.show()

df1.write.mode('overwrite').saveAsTable('HR_DB.HR_SCHEMA.EMP_ID_TX')


