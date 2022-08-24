def print_formatted(number):
    for num in range(1, number + 1):
        decimal_num = num
        octal_num = oct(num)[2:]
        hexadecimal_num = hex(num)[2:]
        binary_num = bin(num)[2:]

        print(f"{' '*(len(str(bin(number))[2:]) - len(str(decimal_num)))}{decimal_num}", end="")

        print(f"{' ' * (len(str(bin(number))[2:]) + 1 - len(str(octal_num)))}{octal_num}", end="")

        print(f"{' ' * (len(str(bin(number))[2:]) + 1 - len(str(hexadecimal_num)))}{hexadecimal_num if hexadecimal_num.isdigit() else hexadecimal_num.upper()}", end="")

        print(f"{' ' * (len(str(bin(number))[2:]) + 1 - len(str(binary_num)))}{binary_num}",end="")
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)