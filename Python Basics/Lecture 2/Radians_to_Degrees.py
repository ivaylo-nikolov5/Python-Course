import math
pi = math.pi
rad = float(input("Rad = "))

deg = rad * 180/pi

result = round(deg)
print("Cel = " + str(result))