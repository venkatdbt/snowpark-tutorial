import snowflake.snowpark as snowpark
import snowflake.snowpark.session as Session
from snowflake.snowpark.functions import col

employee_data = [
[1,'TONY', 101],
[2,'STEVE', 101],
[3,'BRUCE', 102],
[4,'WANDA',102],
[5,'VICTOR',103],
[6,'HANK',105]
]

employee_schema =["ID", "NAME", "DEPT_ID"]

department_data = [
[101, 'HR'],
[102,'SALES'],
[103,'IT'],
[104,'FINANCE']
]

deparment_schema = ['DEPT_ID','DEPT_NAME']

def emp_joins(session: snowpark.Session):
   df_emp = session.createDataFrame(employee_data,employee_schema)
   df_dept = session.createDataFrame(department_data,deparment_schema)
    
   # df_inner = df_emp.join(right=df_dept,
   #                        how='inner',
   #                        on=(df_emp.DEPT_ID == df_dept.DEPT_ID),
   #                        lsuffix='__emp',
   #                        rsuffix='__dept'
   #                       )
   # df_inner = df_emp.join(right=df_dept,
   #                        how='inner',
   #                        on=(df_emp.DEPT_ID == df_dept.DEPT_ID)
   #                       ).select(df_emp.ID,df_emp.NAME.alias('EMP_NAME'),
   #                                df_emp.DEPT_ID.alias('DEPT_ID'),
   #                                df_dept.DEPT_NAME.alias('DEPT_NAME'))

   #join on multiple conditions
   # df_inner = df_emp.join(df_dept,(df_emp.DEPT_ID==df_dept.DEPT_ID)&(df_emp.ID<df_dept.DEPT_ID))
    
   # df_left = df_emp.join(df_dept,df_emp.DEPT_ID==df_dept.DEPT_ID,
   #                       join_type='left',
   #                       lsuffix='_emp',
   #                       rsuffix='_dept')

   # df_left_semi = df_emp.join(df_dept,df_emp.DEPT_ID==df_dept.DEPT_ID,
   #                       join_type='leftsemi',
   #                       lsuffix='_emp',
   #                       rsuffix='_dept')

   df_anti = df_emp.join(df_dept,df_emp.DEPT_ID==df_dept.DEPT_ID,
                         join_type='leftanti',
                         lsuffix='_emp',
                         rsuffix='_dept')
   # df_inner.show(3)
   return df_anti



    

