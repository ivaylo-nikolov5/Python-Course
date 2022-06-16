num1 = int(input())
num2 = int(input())
num3 = int(input())

def min_num(n1, n2, n3):
    min_number = 0
    if n1 < n2 and n1 < n3:
        min_number = n1
    elif n2 < n1 and n2 < n3:
        min_number = n2
    else:
        min_number = n3
    return min_number

print(min_num(num1, num2, num3))