# The Snowpark package is required for Python Worksheets. 
# You can add more packages by selecting them using the Packages control and then importing them.

import snowflake.snowpark as snowpark
from snowflake.snowpark import Window
from snowflake.snowpark.functions import col,rank,dense_rank,lead,lag,min,max

def window_func(session: snowpark.Session): 
    tableName = 'HR_DB.HR_SCHEMA.EMPLOYEES'
    df = session.table(tableName)
    window_spec = Window.partitionBy(col('JOB_ID')).orderBy(col('SALARY').desc())
    df_res = df.withColumn('rnk',rank().over(window_spec))
    return df_res