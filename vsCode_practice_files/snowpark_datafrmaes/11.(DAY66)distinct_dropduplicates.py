# GET THE DISTINCT ROWS and DROP THE DUPLICATES ::


import snowflake.snowpark as snowpark
from snowflake.snowpark import Session

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

data = [ ("James", "Sales", 4000), \
("Michael", "Sales", 4600), \
("Robert", "Sales", 4100), \
("Maria", "Finance", 3000), \
("James", "Sales", 4000), \
("Scott", "Finance", 3300), \
("Scott", "IT", 3300), 
("Jen", "Finance", 3900), \
("Jeff", "Marketing", 3000), \
("Kumar", "Marketing", 2000),
("Saif", "Sales", 4100) \
]


columns= ["employee_name","department", "salary"]

df = new_session.createDataFrame(data,columns)
df.printSchema()

print('original count ===========>'+str(df.count()))

#row level have to remove duplicates
distinctDF = df.distinct()
print('Distinct count ===========>'+str(distinctDF.count()))

#drop duplicates in column level
df1 = df.dropDuplicates()
print('distinct count::'+str(df1.count()))

df2 = df.dropDuplicates(['employee_name','salary'])
print('distinct count for selected cols '+str(df2.count()))