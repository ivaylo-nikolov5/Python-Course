product = input()
day = input()
amount = float(input())

result = 0

if day =="Saturday" or day == "Sunday":
    if product == "banana":
        result = amount * 2.70
    elif product == "apple":
        result = amount * 1.25
    elif product == "orange":
        result = amount * 0.90
    elif product == "grapefruit":
        result = amount * 1.60
    elif product == "kiwi":
        result = amount * 3.00
    elif product == "pineapple":
        result = amount * 5.60
    elif product == "grapes":
        result = amount * 4.20
    else:
        print("Error")

elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if product == "banana":
        result = amount * 2.50
    elif product == "apple":
        result = amount * 1.20
    elif product == "orange":
        result = amount * 0.85
    elif product == "grapefruit":
        result = amount * 1.45
    elif product == "kiwi":
        result = amount * 2.70
    elif product == "pineapple":
        result = amount * 5.50
    elif product == "grapes":
        result = amount * 3.85
    else:
        print("Error")
else:
    print("Error")

print("%.2f" % result)

