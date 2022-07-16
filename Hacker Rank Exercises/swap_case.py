def swap_case(s):
    res = ""
    for el in s:
        if el.isupper():
            res += el.lower()
        else:
            res += el.upper()

    return res


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)