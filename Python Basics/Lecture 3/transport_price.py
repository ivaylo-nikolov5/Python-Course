
km = int(input())
d_a_n = input()

if km < 20 and d_a_n == "day":
    tax = 0.70 + (km * 0.79)
    print(tax)
elif km < 20 and d_a_n == "night":
    tax = 0.70 + (km * 0.90)
    print(tax)
if km >= 20 and km < 100:
    tax = km * 0.09
    print("%.2f" % (tax))
elif km >= 100:
    tax = km * 0.06
    print("%.2f" % (tax))




