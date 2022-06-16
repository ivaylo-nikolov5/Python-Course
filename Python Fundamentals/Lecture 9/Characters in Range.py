def characters(a, b, char:list):
    for i in range(ord(a)+1, ord(b)):
        char.append(chr(i))
    print(" ".join(char))


str1, str2, char_list = input(), input(), []
characters(str1,  str2, char_list)
