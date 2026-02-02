import snowflake.connector as sf
import pandas as pd

sf_user = 'vekt2047'
sf_password = 'Venkata@1245$##'
sf_account = 'ETQLCQX-YO01921'
sf_role = 'ACCOUNTADMIN'
sf_warehouse = 'COMPUTE_WH'
sf_database = 'HR_DB'
sf_schema = 'HR_SCHEMA'

print("User id is       :::"+sf_user)
print("User Password is :::"+sf_password)
print("User Account is  :::"+sf_account)
print("User Role is     :::"+sf_role)
print("User Warehouse is:::"+sf_warehouse)
print("User Database is :::"+sf_database)
print("User Schema is   :::"+sf_schema)


#How to create a context file
ctx = sf.connect(user=sf_user,password=sf_password,account=sf_account,role=sf_role,
                 warehouse=sf_warehouse,database=sf_warehouse,schema=sf_schema)
#cursor
cs = ctx.cursor()

try:
   cs.execute('select * from hr_db.hr_schema.employees')
   df = cs.fetch_pandas_all()
#    df.info()
   for ind in df.index:
       print(ind)
except Exception as e:
    print(e)
finally:
    cs.close()
    print('successfully closed the connection')
ctx.close()