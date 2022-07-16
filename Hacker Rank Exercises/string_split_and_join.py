def split_and_join(string):
    return "-".join(string.split())


if __name__ == '__main__':
    s = input()
    result = split_and_join(s)
    print(result)