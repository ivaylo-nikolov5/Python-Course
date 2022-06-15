lost_fights = int(input())
helmet_price, sword_price, shield_price, armor_price = float(input()), float(input()), float(input()), float(input())

broken_helmets, broken_swords, broken_shields, broken_armors = 0, 0, 0, 0

for i in range(1, lost_fights+1):
    if i % 2 == 0:
        broken_helmets += 1

    if i % 3 == 0:
        broken_swords += 1
        if i % 2 == 0:
            broken_shields += 1
            if broken_shields % 2 == 0:
                broken_armors += 1

total = broken_helmets * helmet_price + broken_swords * sword_price + broken_shields * shield_price + broken_armors * armor_price

print(f"Gladiator expenses: {total:.2f} aureus")



