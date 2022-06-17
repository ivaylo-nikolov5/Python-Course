key = int(input())
lines = int(input())

decrypted_message = ""

for x in range(lines):
    letter = input()
    new_letter = chr(ord(letter) + key)
    decrypted_message += new_letter

print(decrypted_message)