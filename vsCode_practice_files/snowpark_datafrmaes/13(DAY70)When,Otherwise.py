''''
SNOWPARK When Otherwise | SQL Case When Usage

2. Expressions

case when "multiple condition" then "value" end

1.

if fruits == apple:

return "good fruits"

if bike == yamaha

return "its a bike"

else:
NONE/NULL
'''

import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col,when,lit,expr


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

emp_df = new_session.table('HR_DB.HR_SCHEMA.EMPLOYEES')

# emp_df.show()
# emp_df.printSchema()

# emp_res = emp_df.withColumn('JOB_ID_DESCR',when(emp_df.JOB_ID=="IT_PROG","IT PROGRAMMER")\
#                   .when(col("JOB_ID")=='SA_REP','SENIOR ASSOCIATE REPRESENTATIVE')\
#                   .when(col('JOB_ID')=='SA_MA','SENIOR MANAGER')\
#                   .otherwise(emp_df.JOB_ID))

# emp_res = emp_df.withColumn('JOB_ID_DESCR',when(emp_df.JOB_ID=="IT_PROG","IT PROGRAMMER")\
#                   .when(col("JOB_ID")=='SA_REP','SENIOR ASSOCIATE REPRESENTATIVE')\
#                   .when(col('JOB_ID')=='SA_MA','SENIOR MANAGER')\
#                   .otherwise(lit('defalt value')))

# emp_res.select(col('EMPLOYEE_ID'),col('JOB_ID'),col('JOB_ID_DESCR')).show(15)

#multple conditions----------------

# emp_res = emp_df.withColumn('JOB_ID_DESCR',when((emp_df.JOB_ID=='IT_PROG') & (emp_df.FIRST_NAME=='Alexander'),'IT PROGRAMMER')\
#                                            .when((col("JOB_ID")=='SA_REP') |  (col('FIRST_NAME')=='Oliver'),'SENIOR ASSOCIATE REPRESENTATIVE')\
#                                            .otherwise(lit('default_value')))
# emp_res.select(col('FIRST_NAME'),col('JOB_ID'),col('JOB_ID_DESCR')).show(30)

#using sql case when----------------

# df = emp_df.withColumn("JOB_DESCRP",expr("CASE WHEN JOB_ID='IT_PROG' THEN 'IT PROGRAMMER'" + \
#                                               "WHEN JOB_ID='SA_REP'  THEN  'SENIOR ASSOCIATE REPRESENTATIVE'" + \
#                                               "WHEN JOB_ID IS NULL  THEN '' " + \
#                                               "ELSE JOB_ID END"))


# df.select(col('FIRST_NAME'),col('JOB_ID'),col('JOB_DESCRP')).show(30)

# df2 = emp_df.select(col('*'),expr("CASE WHEN JOB_ID='IT_PROG' THEN 'IT PROGRAMMER'" + \
#                                               "WHEN JOB_ID='SA_REP'  THEN  'SENIOR ASSOCIATE REPRESENTATIVE'" + \
#                                               "WHEN JOB_ID IS NULL  THEN '' " + \
#                                               "ELSE JOB_ID END").alias('JOB_DESCRP')) # if we dont mention alias it will make change in original JOB_ID column itself
# df2.select(col('FIRST_NAME'),col('JOB_ID'),col('JOB_DESCRP')).show(30)


emp_df.createOrReplaceTempView('emp_vw') #EXISTS WITH THIS CODE RUN

df = new_session.sql("select FIRST_NAME,JOB_ID,CASE WHEN JOB_ID='IT_PROG' THEN 'IT PROGRAMMER' \
                                              WHEN JOB_ID='SA_REP'  THEN  'SENIOR ASSOCIATE REPRESENTATIVE' \
                                              WHEN JOB_ID IS NULL  THEN '' \
                                              ELSE JOB_ID END as JOB_DESC from emp_vw")
df.show()