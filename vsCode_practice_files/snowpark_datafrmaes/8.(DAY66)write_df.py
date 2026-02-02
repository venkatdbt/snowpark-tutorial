'''WRITE DATA INTO SNOWFLAKE from a SNOWPARK DATAFRAME :::::

DATAFRAMEWRITER CLASS ---- > Methods

1. create a dataframe ---- > (call) DATAFRAME.write property

2. DATAFRAMEWRITER OBJECT

3. WRITE having various mode ("append"), mode ("overwrite") , mode ("errorifexist") , mode(ignore)
4. save as table '''

import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col



connection_params = {
     "account":"ETADEVCQX-YODSTES01921",
     "user":"ventgdg@136",
     "password":"Venkata@@$sg12456",
     "roles":"ACCOUNTADMIN",
     "warehouse":"COMPUTE_WH",
     "database":"HR_DB",
     "schema":"HR_SCHEMA"
}

new_session = Session.builder.configs(connection_params).getOrCreate()

df_dept = new_session.table('HR_DB.HR_SCHEMA.DEPARTMENTS')

# print('the record count is : {0} '.format(df_dept.count()))

df_filter_dept = df_dept.filter(col("DEPARTMENT_NAME")=='Purchasing')

# print(df_filter_dept.count())

df_filter_select = df_filter_dept.drop(col('MANAGER_ID'))

# df_filter_select.show()

df_filter_dept.select(col("DEPARTMENT_ID").alias("DEPT_ID"),col("DEPARTMENT_NAME").alias("Dept_Name"),col("LOCATION_ID").alias("LOC_ID")).show()


# df_filter_dept.write.mode('append').save_as_table("HR_DB.HR_SCHEMA.DEPS")
# df_filter_dept.write.mode('overwrite').save_as_table("HR_DB.HR_SCHEMA.DEPS")
# df_filter_dept.write.mode('errorifexists').save_as_table("HR_DB.HR_SCHEMA.DEPS")
# df_filter_dept.write.mode('ignore').saveAsTable("HR_DB.HR_SCHEMA.DEPS")

#specify tablename types while writing data into snowflake from snowpark dataframe
# permanent,transient,temporary

df_filter_dept.write.mode('ignore').save_as_table("HR_DB.HR_SCHEMA.DEPS_trans",table_type='transient')
df_filter_dept.write.mode('ignore').save_as_table("HR_DB.HR_SCHEMA.DEPS_temp",table_type='temporary')

# create view 
# temporary view

df_filter_dept.create_or_replace_view("HR_DB.HR_SCHEMA.DEPS_VIEW")
df_filter_dept.create_or_replace_temp_view("HR_DB.HR_SCHEMA.DEPS_temp_view")

