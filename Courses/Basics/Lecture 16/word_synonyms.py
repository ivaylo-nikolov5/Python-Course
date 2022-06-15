lines = int(input())
synonyms = {}
for words in range(lines):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = list()

    synonyms[word].append(synonym)

for i in synonyms:
    print(f'{i} - {", ".join(synonyms[i])}')

