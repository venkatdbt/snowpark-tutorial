import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

def main_handler(session: snowpark.Session):
    col_nm = ['col_'+str(i) for i in range(1,7)] #['col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6']
    df = session.createDataFrame([[1,2,3,7,90,98],[23,34,55,78,90,57]],schema=col_nm)
    # df1=df.filter(col("col_1")==23)
    df1=df.where(col("col_1")==23)
    return df1