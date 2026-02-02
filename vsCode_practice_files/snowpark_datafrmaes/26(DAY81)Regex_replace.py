import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col,lit,regexp_replace,when
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

new_session = Session.builder.app_name('regexp-replace').configs(connection_params).getOrCreate()

address = [ (1, "14851 Jeffrey Rd", "DE"),
            (2, "43421 Margarita St", "NY"),
            (3, "13111 Siemon Ave", "CA") ]

schema = ["id", "address", "state"]

def main():
    df = new_session.createDataFrame(address,schema)
    df.show()
    df1 = df.withColumn('ADDRESS_1',regexp_replace(col('ADDRESS'),'[0-9]',''))
    df1.show()

    df2 = df.withColumn('ADDRESS',regexp_replace(col('ADDRESS'),'Rd','Road'))\
            .withColumn('ADDRESS',regexp_replace(col('ADDRESS'),'St','Street'))\
            .withColumn('ADDRESS',regexp_replace(col('ADDRESS'),'Ave','Avenue'))
    df2.show()

    df3 = df.withColumn('ADDRESS',when(df.ADDRESS.endswith('Rd'),regexp_replace(col('ADDRESS'),'Rd','Road'))\
                                 .when(df.ADDRESS.endswith('St'),regexp_replace(col('ADDRESS'),'St','Street'))\
                                 .when(df.ADDRESS.endswith('Ave'),regexp_replace(col('ADDRESS'),'Av','Avenue'))\
                                 .otherwise(df.ADDRESS))
    df3.show()

    df3.write.mode('errorifexists').saveAsTable('HR_DB.HR_SCHEMA.TX_602')

if __name__ == '__main__':
    main()