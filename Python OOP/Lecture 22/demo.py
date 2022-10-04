
from project.bakery import Bakery

my_bakery = Bakery("The Bakers")
print(my_bakery.add_food("Bread", "White Bread", 3))
print(my_bakery.add_food("Cake", "Chocolate Cake", 8))

print(my_bakery.add_drink("Tea", "Ice Tea", 450, "NesTea"))
print(my_bakery.add_drink("Water", "Mineral Water", 500, "Devin"))

print(my_bakery.add_table("InsideTable", 2, 4))
print(my_bakery.add_table("OutsideTable", 52, 2))

print(my_bakery.reserve_table(3))
print(my_bakery.reserve_table(3))

print(my_bakery.order_food(2, "White Bread", "Chocolate Cake", "White Bread", "Chocolate Cake", "Black Bread"
                           , "White Chocolate Cake"))

print(my_bakery.order_drink(52, "Ice Tea", "Mineral Water", "Coffee"))

print(my_bakery.leave_table(2))

