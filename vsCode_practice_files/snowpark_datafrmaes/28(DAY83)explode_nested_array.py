import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.types import StructField,StructType,StringType,LongType,IntegerType
from snowflake.snowpark.functions import col,explode

connection_params = {
    "account":"ETADEVCQX-YODSTES01921",
    "user":"ventgdg@136",
    "password":"Venkata@@$sg12456",
    "roles":"ACCOUNTADMIN",
    "warehouse":"COMPUTE_WH",
    "database":"HR_DB",
    "schema":"HR_SCHEMA"
}

arrayArrayData = [
("James", [ ["Java", "Scala", "C++"], ["Spark", "Jaya"] ]),
("Michael", [["Spark", "Java", "C++"], ["Spark","Java"] ] ),
("Robert", [ ["CSharp", "VB"], ["Spark","Python"] ])
]
schema = ['name','subjects' ]

def main(session:Session):
    new_session = session.builder.app_name('explode_nested_array').configs(connection_params).getOrCreate()
    df = new_session.createDataFrame(arrayArrayData,schema)
    # df.show()
    df.select(col('NAME'),explode(df.SUBJECTS).as_('subjects')).show()
    df.printSchema()


if __name__ == '__main__':
    session = Session
    main(session)