n = int(input())

if n > 7 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
    print("False")
else:
    print("True")