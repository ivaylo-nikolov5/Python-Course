def palindrome(word, idx):
    # if word == word[::-1]:
    #     return f"{word} is a palindrome"
    #
    # return f"{word} is not a palindrome"

    if idx == len(word) // 2:
        return f"{word} is a palindrome"

    left = word[idx]
    right = word[-idx - 1]

    if left != right:
        return f"{word} is not a palindrome"

    return palindrome(word, idx + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))