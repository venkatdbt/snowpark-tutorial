'''
UDFs can be created as anonymous UDFs in Snowpark and assigned to a variable. As long as this
variable is in scope, you can use this variable to call the UDF.

Named Temporary UDFs can be created in Snowpark that are accessible in the same session.
Instead of calling UDF as function, it can be also used as a decorator.

Decorators are a very powerful and useful tool in Python since it
allows programmers to modify the behaviour of a function or class.
Decorators allow us to wrap another function in order to extend
the behaviour of the wrapped function, without permanently
modifying it. But before diving deep into decorators let us
understand some concepts that will come in handy in learning the
decorators.

First Class Objects
In Python, functions are first class objects which means that
functions in Python can be used or passed as arguments.
Properties of first class functions:

. A function is an instance of the Object type.
· You can store the function in a variable.
. You can pass the function as a parameter to another function.
. You can return the function from a function.
. You can store them in data structures such as hash tables, lists,

'''


import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import udf,col
from snowflake.snowpark.types import IntegerType,StringType
import re

connection_params = {
    "account":"ETADEVCQX-YODSTES01921",
    "user":"ventgdg@136",
    "password":"Venkata@@$sg12456",
    "roles":"ACCOUNTADMIN",
    "warehouse":"COMPUTE_WH",
    "database":"HR_DB",
    "schema":"HR_SCHEMA"
}

#if you create decorateor function before session it through error as it is named temporary udf it is in same session only

new_session = Session.builder.configs(connection_params).getOrCreate()

data = [("John$Doe"),("Jane#Smith"),("Senthamizh!Brown")]

df = new_session.createDataFrame(data=data,schema=['name'])
df.show()

df1 = new_session.table('HR_DB.HR_SCHEMA.EMPLOYEES')

#define cleansing function

@udf
def cleanse_name(text:str) -> str:
    #Remove Special charecters using Regular Expressions
    cleansed_text = re.sub(r'[^a-zA-Z0-9\s]','',text)
    return cleansed_text

df.select(col('name'),cleanse_name(col('name')).alias('cleansed_name')).show()

df1.select(col('FIRST_NAME'),cleanse_name(col('FIRST_NAME')).alias('cleansed_name')).show()


@udf
def get_season(date:str)->str:
    _,month,year = date.split('-',2)
    month = int(month)
    if month in (3,4,5):
       return 'spring'
    elif month in (6,7,8):
       return 'Summer'
    elif month in (9,10,11):
       return 'Autumn'
    else:
       return 'Winter'


df1.select(col('HIRE_DATE'),get_season(col('HIRE_DATE'))).show()
