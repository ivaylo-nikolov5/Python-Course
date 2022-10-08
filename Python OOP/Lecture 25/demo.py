from custom_list.custom_list import CustomList

custom_list = CustomList()

print(custom_list.get_list())

custom_list.append(10)
custom_list.append(34)
print(custom_list.get_list())

print(custom_list.remove(1))

try:
    custom_list.remove(9)
except IndexError:
    print("Invalid index! Try again.")

print(custom_list.get(0))

try:
    print(custom_list.get(4))
except IndexError:
    print("Invalid index! Try again.")