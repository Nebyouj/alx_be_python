monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are ${monthly_savings}.")

yearly_savings = monthly_savings * 12
rate = 0.05

projected_savings = yearly_savings + (yearly_savings * 0.05)
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")

