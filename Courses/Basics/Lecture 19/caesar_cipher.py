def caesar_cipher(message):
    encrypted_message = ""
    for x in message:
        encrypted_message += chr(ord(x) + 3)

    print(encrypted_message)


string = input()
caesar_cipher(string)