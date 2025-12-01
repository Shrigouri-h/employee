from employeedetails import employee_info
def test_employee_info():
  expected_output = (
    "Employee Name":" Rahul\n"
    "Employee Id": "EMP1024\n"
    "Department": "Finance\n"
    "Salary": 45000
    )
  assert employee_info("Rahul", "EMP1024", "Finance", 45000) == expected_output
