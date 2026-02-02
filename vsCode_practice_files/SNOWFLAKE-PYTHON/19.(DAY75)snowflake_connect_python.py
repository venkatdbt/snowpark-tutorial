import snowflake.connector as sf

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

print('<----------------------------The cursor Object----------------------------------------->')
print(cs)
print('#################################################################################')

try:
    cs.execute("select current_version(),current_region(),current_user()")
    first_row = cs.fetchone() # fetch oonly first record
    print(first_row,'\n')

    cs.execute('select * from hr_db.hr_schema.employees')
    allrows = cs.fetchall()
    print(allrows,'\n')

    cs.execute('select * from hr_db.hr_schema.employees')
    manyrows = cs.fetchmany(3)
    print(manyrows)

except Exception as e:
    print(e)
finally:
    cs.close()
    print('successfully closed connection')
ctx.close()