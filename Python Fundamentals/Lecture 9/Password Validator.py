def password_validator(password):
    is_valid = True
    is_consist = True
    digits = 0
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", ",", ".", "/", "`", "~", "[", "]",
               "{", "}", "<", ">", "'", ":", ";", "|"]
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    for i in password:
        if i.isdigit():
            digits += 1
        if i in symbols:
            is_valid = False
            is_consist = False

    if not is_consist:
        print("Password must consist only of letters and digits")

    if digits < 2:
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")


passwd = input()
password_validator(passwd)
