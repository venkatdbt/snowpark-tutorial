import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col,lit,substring
from snowflake.snowpark.types import StructField,StructType,StringType,IntegerType,LongType
import logging
import sys

connection_params = {
    "account":"ETADEVCQX-YODSTES01921",
    "user":"ventgdg@136",
    "password":"Venkata@@$sg12456",
    "roles":"ACCOUNTADMIN",
    "warehouse":"COMPUTE_WH",
    "database":"HR_DB",
    "schema":"HR_SCHEMA"
}

new_session = Session.builder.app_name('substring').configs(connection_params).getOrCreate()

data1 = [(1,"20200828"),(2,"20180525")]
schema1 = ["id","date"]

address = [ (1, "14851 Jeffrey Rd", "DE"),
            (2, "43421 Margarita St", "NY"),
            (3, "13111 Siemon Ave", "CA") ]

schema = ["id", "address", "state"]

def main():
    df1 = new_session.createDataFrame(data1,schema1)
    df2 = new_session.createDataFrame(address,schema)
    '''Using sql functions substring'''
    # df1.show()
    df1.withColumn('year',substring(col('date'),1,4))\
       .withColumn('month',substring(col('date'),5,2))\
       .withColumn('day',substring(col('date'),7,2)).show()

    df1.selectExpr('DATE','substring(DATE,1,4) as year'\
                         ,'substring(DATE,5,2) as MONTH'\
                            ,'substring(DATE,7,2)').show()
    df3=df1.withColumn('year',col('DATE').substring(1,4))\
       .withColumn('month',col('DATE').substring(5,2))\
       .withColumn('day',col('DATE').substring(7,2))
    
    df3.show()
   
    df3.write.mode('overwrite').saveAsTable('HR_DB.HR_SCHEMA.TX_01')

if __name__=='__main__':
    main()