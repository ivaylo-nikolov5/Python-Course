def repeat_text(text, times):
    try:
        res = text * int(times)
        print(res)
        return
    except ValueError:
        print("Variable times must be an integer")


string = input()
repeat = input()

repeat_text(string, repeat)
