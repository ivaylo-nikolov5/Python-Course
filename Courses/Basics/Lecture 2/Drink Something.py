age = float(input())

drink = ""

if age <= 14:
    drink = "toddy"
elif 14 < age <= 18:
    drink = "coke"
elif 18 < age <= 21:
    drink = "beer"
else:
    drink = "whisky"

print(f"drink {drink}")

