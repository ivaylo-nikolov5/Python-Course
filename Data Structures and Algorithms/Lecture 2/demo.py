def word_cruncher(idx, target, words_by_idx, words_repeat, used_words):
    if idx >= len(target):
        print(*used_words, sep=" ")
        return
    elif idx not in words_by_idx:
        return

    for word in words_by_idx[idx]:
        if words_repeat[word] == 0:
            continue
        used_words.append(word)
        words_repeat[word] -= 1

        word_cruncher(idx + len(word), target, words_by_idx, words_repeat, used_words)

        used_words.pop()
        words_repeat[word] += 1



elements = input().split(", ")
target = input()

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
            idx = target.index(el, idx)
            if idx not in words_by_idx:
                words_by_idx[idx] = []
            words_by_idx[idx].append(el)
            idx += len(el)
    except ValueError:
        pass

word_cruncher(0, target, words_by_idx, words_repeat, [])
