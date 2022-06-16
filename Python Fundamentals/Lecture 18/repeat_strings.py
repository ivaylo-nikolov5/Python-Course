def repeat_string(string):
    repeat = ""
    for x in string:
        repeat += x * len(x)

    print(repeat)


text = input().split(" ")
repeat_string(text)