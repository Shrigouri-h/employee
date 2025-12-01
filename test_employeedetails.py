from employeedetails import employee_info
def test_employee_info():
  expected_output = (
    "Employee Name: Alice\n"
    "Employee Id: E1001\n"
    "Department: IT\n"
    "Salary: 55000'
    )
  assert employee_info("Alice", "E1001", "IT", 55000) == expected_output
