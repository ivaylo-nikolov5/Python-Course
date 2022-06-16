sectors = int(input())
capacity = int(input())
ticket_price = float(input())

income = capacity * ticket_price
one_sector_inc = income / sectors
charity_money = (income-(one_sector_inc * 0.75))/8

print(f"Total income - {income:.2f} BGN")
print(f"Money for charity - {charity_money:.2f} BGN")
