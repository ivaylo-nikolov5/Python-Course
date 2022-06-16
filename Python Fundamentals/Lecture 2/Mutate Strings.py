word_1 = input()
word_2 = input()

for i in range(len(word_1)):
    if word_1[i] != word_2[i]:
        replacement = word_2[i]
        word = word_1[0:i] + replacement + word_1[i+1:]
        word_1 = word
        print(word_1)