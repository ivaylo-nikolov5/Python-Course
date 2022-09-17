
def reverse_words_order_and_swap_cases(sentence):
    res = ""
    for ch in sentence:
        if ch.isupper():
            res += ch.lower()
        elif ch.islower():
            res += ch.upper()
        else:
            res += ch

    res = reversed(list(res.split()))


    return " ".join(res)

if __name__ == '__main__':
    sentence = "aWESOME is cODING"
    result = reverse_words_order_and_swap_cases(sentence)
    print(result)

