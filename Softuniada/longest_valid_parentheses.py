def longest_valid_parentheses(data):
    longest = 0
    current_longest = 0
    j = 0
    while j < len(data) - 1:
        if data[j] == "(" and data[j + 1] == ")":
            current_longest += 2
            j += 2
        else:

            if current_longest > longest:
                longest = current_longest
            current_longest = 0
            j += 1

    if current_longest > longest:
        longest = current_longest

    return longest




parentheses = input()
print(longest_valid_parentheses(parentheses))