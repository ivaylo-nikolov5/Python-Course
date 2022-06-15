def sum_func(word1, word2):
    total = 0
    for x in range(len(word1)):
        if x < len(word2):
            total += ord(word1[x]) * ord(word2[x])
        else:
            total += ord(word1[x])

    return total


def character_multiplier(words):
    word1 = words[0]
    word2 = words[1]
    result = 0
    if len(word1) > len(word2):
        result = sum_func(word1, word2)
    else:
        result = sum_func(word2, word1)

    print(result)


string = input().split(" ")
character_multiplier(string)
