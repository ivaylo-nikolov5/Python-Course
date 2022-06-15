def validate_usernames(usernames):
    valid_usernames = []

    for x in usernames:
        is_valid = True
        length = len(x)
        if 2 < length <= 16:
            for y in x:
                if not y.isalpha() and not y.isdigit() and y != "-" and y != "_":
                    is_valid = False
                    break
        else:
            is_valid = False

        if is_valid:
            valid_usernames.append(x)

    for x in valid_usernames:
        print(x)


names = input().split(", ")
validate_usernames(names)


#or
import string


def validate_username(usernames):
    allowed_symbols = string.digits + string.ascii_letters + "-" + "_"
    valid_names = []
    for x in usernames:
        is_valid = True
        if 3 > len(x) or 16 < len(x):
            is_valid = False
        elif len([y for y in x if y in allowed_symbols]) != len(x):
            is_valid = False

        if is_valid:
            valid_names.append(x)

    for x in valid_names:
        print(x)


names = input().split(", ")
validate_username(names)