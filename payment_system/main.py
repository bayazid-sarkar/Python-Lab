from payment import calculate_bonus, calculate_tax, calculate_total_payment

salary = float(input("Enter the employee's base salary: "))
bonus = calculate_bonus(salary)
tax = calculate_tax(salary)
total_payment = calculate_total_payment(salary)

print(f"Base Salary: {salary}")
print(f"Bonus(10%): {bonus}")
print(f"Tax Deduction(15%): {tax}")
print(f"Total Payment: {total_payment}")
