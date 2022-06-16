def rage_quit(text):
    unique_symbols = []
    filtered = ""
    repeat = ""
    for x in text:
        if x.lower() not in unique_symbols and not x.isdigit():
            unique_symbols.append(x.lower())
        if x.isdigit():
            filtered += repeat * int(x)
            repeat = ""
        else:
            repeat += x

    if len(filtered) == 0:
        filtered += repeat

    print(f"Unique symbols used: {len(unique_symbols)}")
    print(filtered.upper())


string = input().lower()
rage_quit(string)