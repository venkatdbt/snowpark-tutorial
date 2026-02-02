import snowflake.snowpark as snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col,approx_count_distinct,avg,\
                                         collect_set,count_distinct,\
                                         max,min,mean,median,stddev,stddev_samp,\
                                         stddev_pop,sum,sum_distinct,count

connection_params = {
    "account":"ETADEVCQX-YODSTES01921",
    "user":"ventgdg@136",
    "password":"Venkata@@$sg12456",
    "roles":"ACCOUNTADMIN",
    "warehouse":"COMPUTE_WH",
    "database":"HR_DB",
    "schema":"HR_SCHEMA"
}

simpleData = [ ("James", "Sales", 3000),
("Michael", "Sales", 4600),
("Robert", "Sales", 4100),
("Maria", "Finance", 3000),
("James", "Sales", 3000),
("Scott", "Finance", 3300),
("Jen", "Finance", 3900),
("Jeff","Marketing", 3000),
("Kumar", "Marketing", 2000),
("Saif", "Sales", 4100)
]
schema = ["employee_name", "department", "salary"]

def main(session:Session):  #argument:type
    new_session = session.builder.app_name('aggregate_funcs').configs(connection_params).getOrCreate()
    df = new_session.createDataFrame(simpleData,schema)
    df.show()
    ##aggregation functions in snowpark dataframe

    print("approx_count_distinct:::::{}".format(df.select(approx_count_distinct(col('SALARY'))).collect()[0][0]))

    print('SALARY avg ::::' + str(df.select(avg(col('SALARY'))).collect()[0][0]))

    print('COUNT ::::' + str(df.select(count(col('SALARY'))).collect()[0][0]))

    df.select(collect_set(col('SALARY')),collect_set(col('DEPARTMENT'))).show()  #collect set ignore null values and duplicates

    df.select(count_distinct(col('SALARY'),col('DEPARTMENT'))).show() #COMBINATION DISTINCT VALUES

    print("max salary is {}".format(df.select(max(col("salary"))).collect()[0][0]))
    print("min salary is {}".format(df.select(min(col("salary"))).collect()[0][0]))
    print("mean salary is {}".format(df.select(mean(col("salary"))).collect()[0][0]))
    print("median of salary is {}".format(df.select(median(col("salary"))).collect()[0][0]))
    print("std value is {}".format(df.select(stddev(col("salary"))).collect()[0][0]))
    print("total salary value is {}".format(df.select(sum(col("salary"))).collect()[0][0]))
    print("sum distinct salary value is {}".format(df.select(sum_distinct(col("salary"))).collect()[0][0]))


if __name__ == '__main__':
    session = Session
    main(session)