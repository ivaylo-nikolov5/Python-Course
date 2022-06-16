def replace_repeating_chars(info):
    filtered = ""

    for x in range(len(info)):
        if x != len(info)-1:
            if info[x] != info[x+1]:
                filtered += info[x]
        else:
            filtered += info[x]

    print(filtered)


text = input()
replace_repeating_chars(text)