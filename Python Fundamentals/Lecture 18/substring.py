def substrings(chars, string):

    while chars in string:
        string = string.replace(chars, "")

    print(string)


characters = input()
text = input()

substrings(characters, text)
