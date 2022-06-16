def emoticon_finder(text):
    for x in range(len(text)):
        if text[x] == ":":
            print(f":{text[x+1]}")


string = input()
emoticon_finder(string)