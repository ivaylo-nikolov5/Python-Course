string = input()
repeat = int(input())

def str_rep(strn, rep):
    rep_str = ""
    for i in range(0, rep):
        rep_str += f"{strn}"
    return rep_str

print(str_rep(string, repeat))
