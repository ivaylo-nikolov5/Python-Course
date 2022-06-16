import math

hours = int(input())
minutes = int(input())

total_minutes = hours * 60 + minutes + 15

new_hours = total_minutes / 60
new_minutes = total_minutes % 60

if new_hours >= 24:
    new_hours = 0

new_hours = math.floor(new_hours)

if new_minutes < 10:
    print(str(new_hours)+":0"+str(new_minutes))
else:
    print(str(new_hours)+":"+str(new_minutes))