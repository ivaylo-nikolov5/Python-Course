num = float(input())
first = input()

# m, mm, cm, mi, in, km, ft, yd
if first == "m":
    second = input()
    if second == "mm":
        print(num * 1000)
    elif second == "cm":
        print(num * 100)
    elif second == "mi":
        print(num * 0.000621371192 )
    elif second == "in":
        print(num * 39.3700787 )
    elif second == "km":
        print(num * 0.001 )
    elif second == "ft":
        print(num * 3.2808399  )
    elif second == "km":
        print(num * 1.0936133  )


if first == "mm":
    second = input()
    if second == "m":
        print(num / 1000)
    elif second == "cm":
        print(num / 10)
    elif second == "mi":
        print(num * 0.621371192)
    elif second == "in":
        print(num * 39.3700787 )
    elif second == "km":
        print(num * 0.001 )
    elif second == "ft":
        print(num * 3.2808399  )
    elif second == "km":
        print(num * 1.0936133  )



