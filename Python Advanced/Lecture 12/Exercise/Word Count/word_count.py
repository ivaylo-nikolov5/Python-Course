import re

with open("words.txt") as words_text:
    words = [word for word in words_text.read().split()]


with open("input.txt") as input_:
    text = input_.read()
    words_count = dict()
    for word in words:
        pattern = fr"\b{word}\b"
        count = len(re.findall(pattern, text, re.IGNORECASE))

        words_count[word] = count


words_count = dict(sorted(words_count.items(), key=lambda x: -x[1]))

with open("output.txt" , "w") as output:
    for key, value in words_count.items():
        output.writelines(f"{key} - {value}\n")



