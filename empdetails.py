def employee_info(name, emp_id, department, salary):
    return f"Employee Name: {name}\nEmployee ID: {emp_id}\nDepartment: {department}\nSalary: ₹{salary}"

if __name__ == "__main__":
    name = "Rahul"
    emp_id = "EMP1024"
    department = "Finance"
    salary = 45000

    print("Employee Details:\n")
    print(employee_info(name, emp_id, department, salary))
