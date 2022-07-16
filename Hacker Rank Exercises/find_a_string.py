def count_substring(string, sub_string):
    sub_string_count = string.count(sub_string)
    return sub_string_count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)