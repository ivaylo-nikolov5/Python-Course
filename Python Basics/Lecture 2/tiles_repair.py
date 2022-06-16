n = float(input("дължината на страна от площадката:"))
w = float(input("широчината на една плочка: "))
l = float(input("дължината на една плочка: "))
m = float(input("широчината на пейката: "))
o = float(input("дължината на пейката "))

total_area = n * n
bench_area = m * o
covering_area = total_area - bench_area
tiles_area = w * l

needed_tiles = covering_area / tiles_area
needed_time = needed_tiles * 0.2

print("---------------------------------------")

print("Необходими плочки: " + str(needed_tiles))
print("Необходимо време: " + str(needed_time))