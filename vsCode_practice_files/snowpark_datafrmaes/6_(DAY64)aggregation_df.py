import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from   snowflake.snowpark.functions import *

connection_params = {
     "account":"ETADEVCQX-YODSTES01921",
     "user":"ventgdg@136",
     "password":"Venkata@@$sg12456",
     "roles":"ACCOUNTADMIN",
     "warehouse":"COMPUTE_WH",
     "database":"HR_DB",
     "schema":"HR_SCHEMA"
}

new_session = Session.builder.configs(connection_params).create()

print(new_session.sql('select current_schema()').collect())

df_emp = new_session.table("EMPLOYEES")
df_emp.show(n=5)

df_countries = new_session.table("COUNTRIES")
df_countries.show()

print(df_countries.collect(),'\n')
