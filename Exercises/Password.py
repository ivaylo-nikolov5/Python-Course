username = input()
password = input()

ver_password = input()
while ver_password != password:
    ver_password = input()
print(f"Welcome {username}!")

