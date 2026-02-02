import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
# from snowflake.snowpark.functions import union,unionAll

simpleData = [ ("James", "Sales", "NY", 90000, 34, 10000) , \
("Michael", "Sales", "NY", 86000, 56, 20000) ,
("Robert", "Sales", "CA", 81000, 30, 23000) ,
("Maria", "Finance", "CA", 90000, 24, 23000) \
]

columns= ["employee_name", "department", "state", "salary", "age", "bonus"]

simpleData2 = [("James", "Sales", "NY", 90000, 34, 10000) , \
("Maria", "Finance", "CA", 90000, 24, 23000), \
("Jen", "Finance", "NY", 79000, 53, 15000), \
("Jeff", "Marketing", "CA", 80000, 25, 18000), \
("Kumar", "Marketing", "NY", 91000, 50, 21000) \
]

columns2= ["employee_name", "department", "state", "salary", "age", "bonus"]

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

df1 = new_session.createDataFrame(simpleData,columns)
df2 = new_session.createDataFrame(simpleData2,columns2)

# df1.show()

df1.printSchema()

df1.union(df2).show()

df1.unionAll(df2).show()
