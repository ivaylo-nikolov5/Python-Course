import math

money = float(input())
width_floor = float(input())
length_floor = float(input())
tile_side = float(input())
tile_height = float(input())
tile_price = float(input())
workman_salary = float(input())

floor_area = width_floor * length_floor
tile_area = tile_side * tile_height/2
needed_tiles = floor_area / tile_area
needed_tiles = math.ceil(needed_tiles)
needed_tiles = needed_tiles + 5

sum = needed_tiles * tile_price + workman_salary

diff = abs(money - sum)

if sum <= money:
    print(f"{diff:.2f} lv left.")
else:
    print(f"You'll need {diff:.2f} lv more.")