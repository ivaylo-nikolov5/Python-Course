budget = float(input())
season = input()

destination = ""
holiday_info = ""
spent_money = 0.00


if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent_money = budget * 0.30
        holiday_info = "Camp"
    else:
        spent_money = budget * 0.70
        holiday_info = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent_money = budget * 0.40
        holiday_info = "Camp"
    else:
        spent_money = budget * 0.80
        holiday_info = "Hotel"
else:
    destination = "Europe"
    spent_money = budget * 0.90
    holiday_info = "Hotel"

print(f"Somewhere in {destination}")
print(f"{holiday_info} - {spent_money:.2f}")