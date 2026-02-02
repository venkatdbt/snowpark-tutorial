def ODD_EVEN(emp_id:int)->str:
    if emp_id%2==0:
       return str(emp_id) + ' is a EVEN EMP_ID'
    else:
       return str(emp_id) + ' is a ODD EMP_ID'
    

# employees = [
# {"name":"sathish","age":32,"department":"IT"},
# {"name":"arif","age":34,"department":"FINANCE"},
# {"name":"anand","age":38,"department":"RECRUITMENT"}
# ]

def filter_emp_salary(emp:int)->list:
    filtered_employees = [emp['name'] for emp in employees if emp['age']>32]
    return filtered_employees


# if __name__ == "__main__":
#     print(filter_emp_salary(employees))