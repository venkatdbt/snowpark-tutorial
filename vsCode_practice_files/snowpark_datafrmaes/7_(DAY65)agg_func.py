import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import max,min,avg,mean,col


connection_params = {
     "account":"ETADEVCQX-YODSTES01921",
     "user":"ventgdg@136",
     "password":"Venkata@@$sg12456",
     "roles":"ACCOUNTADMIN",
     "warehouse":"COMPUTE_WH",
     "database":"HR_DB",
     "schema":"HR_SCHEMA"
}

employee_data = [
[1,'TONY',24000],
[2,'STEVE', 17000],
[3,'BRUCE', 9000],
[4,'WANDA',20000],
[5,'VICTOR', 12000],
[6,'STEPHEN', 10000]
]

employee_schema = ["EMP_ID", "EMP_NAME", "SALARY"]

new_session = Session.builder.configs(connection_params).getOrCreate()

emp_df = new_session.createDataFrame(employee_data,employee_schema)

# print(f"the employee count is: {emp_df.count()}")

# emp_df.agg(max("SALARY").alias('maxxx'),min("SALARY"),avg("SALARY")).show()
emp_df.agg(max(col("SALARY")).alias('maxxx'),min(col("SALARY")),avg(col("SALARY"))).show()

##passing a typle with column names and aggregation functions
# emp_df.agg(("SALARY","max"),("SALARY","min"),("SALARY","mean")).show()

#passing a list of columns objects and tuple
emp_df.agg([('SALARY','max'),('SALARY','min'),('SALARY','mean')]).show()

#passing a dictionay mapping column name to aggregate functions
emp_df.agg({'SALARY':'min',"EMP_ID":"max"}).show()

#aggregate functions using DataFrame.select method
emp_df.select(min("SALARY").as_('min_sal'),max("SALARY").as_('max_sal')).show()

results_df=emp_df.agg(max(col("SALARY")).alias('maxxx'),min(col("SALARY")).as_('min_sal'),avg(col("SALARY")))

## DataFrame.collect (return list of row objects)
results = emp_df.agg(max(col("SALARY")).alias('maxxx'),min(col("SALARY")).as_('min_sal'),avg(col("SALARY"))).collect()
print(results)

results_df.write.save_as_table("employee_agg")

