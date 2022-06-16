number = int(input())
position = int(input())

to_binary = list(map(str, bin(number)))
to_binary[-position-1] = 0
to_binary.remove(to_binary[0])
to_binary.remove(to_binary[0])
to_binary = "".join(to_binary)


def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    print(decimal)


binary_to_decimal(to_binary)