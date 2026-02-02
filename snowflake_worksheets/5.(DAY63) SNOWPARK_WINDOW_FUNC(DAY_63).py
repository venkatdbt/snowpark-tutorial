import snowflake.snowpark as snowpark
import snowflake.snowpark.session as Session
from snowflake.snowpark import Window
from snowflake.snowpark.functions import col,row_number,desc,sum,lit,min,rank,dense_rank,lag,lead

employee_data = [
[1,'TONY',24000,101],
[2,'STEVE',17000,101],
[3,'BRUCE',9000,101],
[4,'WANDA',20000, 102],
[5,'VICTOR',12000,102],
[6,'STEPHEN',10000,103],
[7,'HANK',15000,103],
[8,'THOR',21000,103]
]

employee_schema = ["EMP_ID", "EMP_NAME", "SALARY", "DEPT_ID"]

def window_handler(session: snowpark.Session): 
    df_emp = session.createDataFrame(employee_data,employee_schema)
    
    #create a windows specifications
    window_spec = Window.partitionBy(col("DEPT_ID")).orderBy(col("SALARY").desc())
    
    # df = df_emp.withColumn('rn',row_number().over(window_spec)).where(col('rn')==1).sort(col("DEPT_ID"))
    # df_final = df.drop(col('rn')) 

    #total salary
    # df_final = df_emp.withColumn('tot_sal',sum(col('SALARY')).over(window_spec))\
    #                  .with_column_renamed('tot_sal','TOTAL_SALARY')\
    #                  .withColumn('constant',lit('VENKAT'))
    #-----------------------------------------------------------
    # cumulative salary
    # window_spec1 = Window.partitionBy(col('DEPT_ID')).orderBy(col("EMP_ID")).rowsBetween(Window.currentRow,3)
    # df_final = df_emp.withColumn('CUM_SAL',sum(col('SALARY')).over(window_spec1))
    # df_final = df_emp.withColumn('MIN_SAL',min('SALARY').over(window_spec1)).sort(col('EMP_ID'))
    #-----------------------------------------------------------
    window_spec3 = Window.partitionBy(col('DEPT_ID')).orderBy(col('SALARY').desc())
    df_final = df_emp.with_column('rnk',rank().over(window_spec3)).sort(col("EMP_ID"))
    df_final = df_final.withColumn('dense_ranke',dense_rank().over(window_spec3)).sort(col('EMP_ID'))
    df_final = df_final.withColumn('lag',lag(col('SALARY'),1).over(window_spec3)).sort(col('EMP_ID'))
    df_final = df_final.withColumn('lead',lead(col('SALARY'),1).over(window_spec3)).sort(col('EMP_ID'))
    return df_final






    

    # drop,withColumn,with_column_renamed,lit














    