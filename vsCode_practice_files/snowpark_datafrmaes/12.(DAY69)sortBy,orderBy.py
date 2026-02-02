'''ORDER BY performs a total ordering of the query result set. This means that
all the data is passed through a single reducer, which may take an
unacceptably long time to execute for larger data sets.

SORT BY orders the data only within each reducer, thereby performing a
local ordering, where each reducer's output will be sorted. You will not
achieve a total ordering on the dataset. Better performance is traded for total
ordering.'''   

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

df_emp=new_session.table('HR_DB.HR_SCHEMA.EMPLOYEES')

# df_emp.show()

# df_emp.orderBy(col('EMPLOYEE_ID').desc(),col('JOB_ID').desc()).show()
# df_emp.orderBy(col('EMPLOYEE_ID').asc()).select(col('EMPLOYEE_ID'),col('JOB_ID')).show()

# df_emp.sort(col('EMPLOYEE_ID').desc(),col('JOB_id').desc()).select(col('EMPLOYEE_ID'),col('JOB_ID')).show()
# df_emp.sort(col('EMPLOYEE_ID').desc(),col('JOB_id').desc()).select(col('*')).show() # all columns

#we can also write as 
df_emp.sort(col('EMPLOYEE_ID'),col('JOB_ID'),ascending=['FALSE','FALSE']).show()  #FALSE:DESC,TRUE:ASC
df_emp.sort('EMPLOYEE_ID','JOB_ID',ascending=['FALSE','FALSE']).show()  #FALSE:DESC,TRUE:ASC


# df_emp.sort(col('COMMISSION_PCT').asc_nulls_first()).select(col('COMMISSION_PCT')).show(30)

#with col func
# df_emp.sort(df_emp.COMMISSION_PCT.asc_nulls_first()).select(df_emp.COMMISSION_PCT).show(30)


df_emp.createOrReplaceTempView("emp_temp_vw") #this view exists untill this code in running state


new_session.sql("select * from emp_temp_vw order by JOB_ID desc").show() # using sql leads more performence issue


new_session.close()

#how this below code fails as it is temp view
new_session.sql("select * from emp_temp_vw order by JOB_ID desc").show() # using sql leads more performence issue