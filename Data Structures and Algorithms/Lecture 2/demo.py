def find_all_combinations(idx, target, words_by_index, words_repeat, combinations):
    if idx >= len(target):
        print(*combinations, sep=" ")
        return
    if idx not in words_by_index:
        return
    for word in words_by_index[idx]:
        if words_repeat[word] == 0:
            continue

        combinations.append(word)
        words_repeat[word] -= 1

        find_all_combinations(idx + len(word), target, words_by_index, words_repeat, combinations)

        combinations.pop()
        words_repeat[word] += 1

elements = input().split(", ")
target = input()

words_by_index = {}
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
            if idx not in words_by_index:
                words_by_index[idx] = []
            words_by_index[idx].append(el)
            idx += len(el)
    except ValueError:
        pass


find_all_combinations(0, target, words_by_index, words_repeat, [])