def sorting(string):
    digits = ""
    letters = ""
    others = ""

    for x in string:
        if x.isdigit():
            digits += x
        elif x.islower() or x.isupper():
            letters += x
        else:
            others += x

    print(digits)
    print(letters)
    print(others)

            
text = input()

sorting(text)