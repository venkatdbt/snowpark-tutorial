import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import udf,col,lit
from snowflake.snowpark.types import IntegerType,StringType,FloatType,DateType
import datetime 

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

# def calculate_exp(hire_date:str)->str:
#     hire_date = datetime.strptime(str(hire_date).replace(' ',''),'%Y-%m-%d').date() #strptime - string parse time
#     today = datetime.date.today().date() # 11-05-2026
#     year_exp = today.year - hire_date.year
#     return str(year_exp)

def calculate_exp(hire_date_str:str) ->str :
    hire_date = datetime.datetime.strptime(str(hire_date_str),'%Y-%m-%d').date()
    today = datetime.datetime.today().date()
    years_exp = today.year - hire_date.year
    return years_exp

new_session.udf.register(
    func=calculate_exp,
    name='CAL_EXP',
    return_type=StringType(),
    input_types=[StringType()],
    is_permanent=True,
    replace=True,
    stage_location='@SNOWPARK_UDF'  # Ensure this stage exists
)

emp_df = new_session.table('HR_DB.HR_SCHEMA.EMPLOYEES')

emp_df.select(col('EMPLOYEE_ID'),col('HIRE_DATE'),calculate_exp(col('HIRE_DATE')).as_('exprerience_years')).show()