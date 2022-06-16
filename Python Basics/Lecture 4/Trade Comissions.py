town = input("Town: ")
s = float(input("S: "))
result = 0

if town == "Sofia":
    if 0 <= s <= 500:
        result = s * 0.05
    elif 500 < s <= 1000:
        result = s * 0.07
    elif 1000 < s <= 10000:
        result = s * 0.08
    else:
        result = s * 0.12

elif town == "Varna":
    if 0 <= s <= 500:
        result = s * 0.045
    elif 500 < s <= 1000:
        result = s * 0.075
    elif 1000 < s <= 10000:
        result = s * 0.10
    else:
        result = s * 0.13

elif town == "Plovdiv":
    if 0 <= s <= 500:
        result = s * 0.055
    elif 500 < s <= 1000:
        result = s * 0.08
    elif 1000 < s <= 10000:
        result = s * 0.12
    else:
        result = s * 0.145

else:
    result = "error"

if type(result) == str or s < 0:
    print(result)
else:
    print(("{:.2f}".format(result)))


