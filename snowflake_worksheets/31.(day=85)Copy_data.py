# The Snowpark package is required for Python Worksheets. 
# You can add more packages by selecting them using the Packages control and then importing them.

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col,count
from snowflake.snowpark.types import StructField,StructType,IntegerType,StringType,DecimalType

schema = StructType(
    [
    StructField('category',StringType(),True),
    StructField('product_id',StringType(),True),
    StructField('productname',StringType(),True),
    StructField('subcategory',StringType(),True)
    ]) 

def copy_data(session: snowpark.Session): 
    df_products = session.read.schema(schema).options({'skip_header':1,'field_delimiter':','}).csv('@"HR_DB"."HR_SCHEMA"."PIPER_DETAILS"/products.csv')
    copied_df_table = df_products.copy_into_table('HR_DB.HR_SCHEMA.PRODUCTS_INFO',force=True,on_error="continue",files=['products.csv'])
    cnt = session.table('HR_DB.HR_SCHEMA.PRODUCTS_INFO').count()
    print(cnt)
    # Return value will appear in the Results tab.
    return df_products

    