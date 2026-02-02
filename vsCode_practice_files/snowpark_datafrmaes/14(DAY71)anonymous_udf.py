import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import udf,col
from snowflake.snowpark.types import StringType

connection_params = {
    "account":"ETADEVCQX-YODSTES01921",
    "user":"ventgdg@136",
    "password":"Venkata@@$sg12456",
    "roles":"ACCOUNTADMIN",
    "warehouse":"COMPUTE_WH",
    "database":"HR_DB",
    "schema":"HR_SCHEMA"
}

#input - snowpark is lazily evaluated (first letter of each word should be uppercase)
def convertcase(input): 
   restr=''
   arr = input.split(" ")
   for x in arr:
      restr = restr + x[0].upper() + x[1:] + " "
   return restr


def lowercase(input): 
   restr=''
   arr = input.split(" ")
   for x in arr:
      restr = restr + x[0].lower() + x[1:] + " "
   return restr


new_session = Session.builder.app_name('udf_funtion')\
                     .configs(connection_params).getOrCreate()

##anonymouse udf
convert_upper_case = udf(func=convertcase,return_type=StringType(), input_types=[StringType()])
conver_lower_case = udf(func=lowercase,return_type=StringType(),input_types=[StringType()])


# df = new_session.createDataFrame(data=['welcome to india','welcome to japan'],schema=['comment'])
# df.show()

# df.select(col('comment'),convert_upper_case(col('comment')).as_('case_comment')).show() #as_ , alias


df_emp = new_session.table("HR_DB.HR_SCHEMA.EMPLOYEES")
df_emp.show(3)
df_employee = df_emp.select(col('FIRST_NAME'),conver_lower_case(col('FIRST_NAME')).alias('TX_FIRST_NAME'))
df_employee.show(3)
df_employee.write.mode('overwrite').saveAsTable('HR_DB.HR_SCHEMA.EMPLOYEES_34')