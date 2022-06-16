n = int(input())

def print_header(num):
    print("-"*2*num)

def print_body(num):
    for i in range(0, num-2):
        print("-"+"\\/"*(num-1)+"-")

def print_square():
    print_header(n)
    print_body(n)
    print_header(n)

print_square()

