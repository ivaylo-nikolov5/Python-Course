number = int(input())
word = input()

word_list = []
filtered = []

for i in range(number):
    string = input()
    word_list.append(string)
    if word in string:
        filtered.append(string)


print(f"{word_list}\n{filtered}")

