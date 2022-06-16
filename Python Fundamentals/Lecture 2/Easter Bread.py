budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = flour_price + (flour_price * 0.25)
milk_for_one_bread = milk_price * 0.25
bread_price = eggs_price + flour_price + milk_for_one_bread

bread_count = int(budget // bread_price)

current_bread_count = 0
colored_eggs = 0

for i in range(1, bread_count+1):
    current_bread_count += 1
    colored_eggs += 3
    if current_bread_count % 3 == 0:
        colored_eggs -= current_bread_count - 2

left_money = budget - (bread_count * bread_price)

print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {left_money:.2f}BGN left.")
