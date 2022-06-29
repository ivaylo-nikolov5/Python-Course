tabs = int(input())
salary = int(input())

left_money = salary

for i in range(tabs):
    website = input()
    if website == "Facebook":
        left_money -= 150
    elif website == "Instagram":
        left_money -= 100
    elif website == "Reddit":
        left_money -= 50

    if left_money <= 0:
        print("You have lost your salary.")
        break

if salary == left_money:
    print(salary)
elif left_money <= 0:
    pass
else:
    print(f"{(left_money)}")
