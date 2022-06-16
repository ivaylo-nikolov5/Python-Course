def rage_quit(text):
    unique_symbols = []
    message = ""
    repeat = ""
    for x in text:
        if x.lower() not in unique_symbols and not x.isdigit():
            unique_symbols.append(x.lower())

        if x.isdigit():
            message += repeat * int(x)
            repeat = ""
        else:
            repeat += x
    print(f"Unique symbols used: {len(unique_symbols)}")
    print(message.upper())

string = input()
rage_quit(string)