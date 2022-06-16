import math

name = input()
budget = float(input())
beer_bottles = int(input())
chips_packets = int(input())

beer_price = 1.2 * beer_bottles
chips_price = 0.45 * beer_price
total_chips_price = chips_price * chips_packets
total_chips_price = math.ceil(total_chips_price)

total = beer_price + total_chips_price

diff = abs(total - budget)

if total <= budget:
    print(f"{name} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name} needs {diff:.2f} more leva!")