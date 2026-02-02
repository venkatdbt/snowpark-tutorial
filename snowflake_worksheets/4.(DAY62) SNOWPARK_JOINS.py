import snowflake.snowpark as snowpark
import snowflake.snowpark.session as Session
from snowflake.snowpark.functions import col

def main(session: snowpark.Session): 
    tableName_emp = 'HR_DB.HR_SCHEMA.EMPLOYEES'
    df_emp = session.table(tableName_emp)
    tableName_dept = 'HR_DB.HR_SCHEMA.DEPARTMENTS'
    df_dept = session.table(tableName_dept)

    df_job_hist = session.table('HR_DB.HR_SCHEMA.JOB_HISTORY')

    df_join_res = df_emp.join(df_dept,
                           df_emp['DEPARTMENT_ID']==df_dept['DEPARTMENT_ID'],
                           join_type='full')

    df_final_res = df_join_res.join(df_job_hist,
                           df_join_res['EMPLOYEE_ID']==df_job_hist['EMPLOYEE_ID'],
                           join_type='semi')
    # df_inner.show()
    return df_final_res




    