def word_cruncher(idx, word, words_by_idx, words_repeat, used_words):
    if idx >= len(word):
        print(*used_words)
        return

    if idx not in words_by_idx:
        return

    for i in words_by_idx[idx]:
        if words_repeat[i] == 0:
            continue
        used_words.append(i)
        words_repeat[i] -= 1

        word_cruncher(idx + len(i), word, words_by_idx, words_repeat, used_words)

        words_repeat[i] += 1
        used_words.pop()


elements = input().split(", ")
word = input()

words_by_idx = {}
words_repeat = {}

for el in elements:
    if el in words_repeat:
        words_repeat[el] += 1
        continue

    words_repeat[el] = 1

    try:
        idx = 0
        while True:
            idx = word.index(el, idx)
            if idx not in words_by_idx:
                words_by_idx[idx] = []
            words_by_idx[idx].append(el)
            idx += len(el)

    except ValueError:
        pass


word_cruncher(0, word, words_by_idx, words_repeat, [])
