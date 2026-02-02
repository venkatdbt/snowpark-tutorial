# The Snowpark package is required for Python Worksheets. 
# You can add more packages by selecting them using the Packages control and then importing them.

import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col,count,max,min

employee_data = [
    [1,'anand',202],
    [2,'steve',303],
    [3, 'bruce', 403],
    [4, 'wanda',508],
    [5,'suji', 512],
    [6,'steve', 615],
    [7,'tamil',814],
    [8,'victor', 913],
    [8,'victor', 913],
    [6,'steve', 615],
]

employee_schema = ["ID", "NAME", "DEPT_ID"]

def main(session: snowpark.Session):
    df_emp = session.createDataFrame(employee_data,employee_schema)
    # df_emp_filter = df_emp.filter(col("ID")==1)
    # df_emp_filter = df_emp.filter(col("ID").in_(1,3,7,8))
    # df_emp_filter = df_emp.filter(col("ID").isin(1,3,7,8))
    # df_emp_filter = df_emp.filter(col('NAME')=='victor').select(col("ID").alias('emp_id'),col("DEPT_ID").alias('department_id'))
    # df_emp_filter = df_emp.filter(~col('ID').in_('1'))
    # df_emp_filter = df_emp.filter(col("ID").is_null())
    # df_emp_filter = df_emp.filter(col("ID").is_not_null())
    # return df_emp_filter

    df_group_by = df_emp.group_by(col("NAME")).agg(count("ID"),max("DEPT_ID"),min("DEPT_ID"))
    return df_group_by    

    
    