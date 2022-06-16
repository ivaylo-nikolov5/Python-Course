key = int(input())
number_of_line = int(input())

encrypted_message = ""

for i in range(number_of_line):
    letter = input()
    ord_letter = ord(letter)
    sum_ord_letter = ord_letter + key
    new_letter = chr(sum_ord_letter)
    encrypted_message += new_letter

print(encrypted_message)
