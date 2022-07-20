string = input()

alphanum = False
alphabetical = False
digits = False
lowercase = False
uppercase = False

for el in string:
    if el.isalnum():
        alphanum = True
    if el.isalpha():
        alphabetical = True
        if el.islower():
            lowercase = True
        else:
            uppercase = True
    elif el.isdigit():
        digits = True
print(alphanum)
print(alphabetical)
print(digits)
print(lowercase)
print(uppercase)

