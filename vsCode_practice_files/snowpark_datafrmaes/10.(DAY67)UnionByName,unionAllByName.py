import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
# from snowflake.snowpark.functions import union,unionAll

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

data = [("James",34), ("Anand",30),("Michael",56),("Robert",45),("Arif",67)]

columns = ["name","age"]

df = new_session.createDataFrame(data=data,schema=columns)

df.printSchema()


data1 = [(34,"James"),(30,"Anand"),(56,"Michae1"),(45,"Robert"),(67,"Arif")]

columns_1= ["age","name"]

df1 = new_session.createDataFrame(data=data1,schema=columns_1)

df1.printSchema()

#here in df1 columns are not in same order as df

df.unionByName(df1).show()

df.unionAllByName(df1).show()