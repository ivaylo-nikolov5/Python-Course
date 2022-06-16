n = int(input("Working days = "))
m = float(input("Money per day = "))
d = float(input("Dollar course = "))

monthly_salary = n * m
yearly_salary = (monthly_salary * 12) + (monthly_salary * 2.5)

tax = yearly_salary * 0.25
clear_yearly_income_d = yearly_salary - tax
clear_yearly_income_l = clear_yearly_income_d * d

average_day_profit = clear_yearly_income_l / 365

print("%.2f" % (average_day_profit))

