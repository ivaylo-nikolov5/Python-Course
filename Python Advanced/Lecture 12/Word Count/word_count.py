import re

words_count = dict()
searched_words = []

with open("words.txt") as words:
    searched_words = words.read().split()

with open("input.txt") as input_:
    text = input_.read()
    for word in searched_words:
        pattern = fr"\b{word}\b"
        count = len(re.findall(pattern, text, re.IGNORECASE))
        words_count[word] = count

with open("output.txt", "w") as output:
    words_count = dict(sorted(words_count.items(), key=lambda x: -x[1]))
    for word, times in words_count.items():
        output.writelines(f"{word} - {times}\n")



