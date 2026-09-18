employee_name = input("Enter the employees name: ")
hours_worked = float(input("Enter the number of hours worked: "))
hourly_pay = float(input("Enter the hourly pay rate: "))
tax_rate = float(input("Enter the tax rate: "))

gross_pay = hours_worked * hourly_pay
tax_withheld = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_withheld

print(f"Employee: {employee_name}")
print(f"Gross pay: ${gross_pay:.2f}")
print(f"Tax withheld: ${tax_withheld:.2f}")
print(f"Net pay: ${net_pay:.2f}")