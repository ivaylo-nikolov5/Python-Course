word = input()

letters = []
capitals = []

for x in word:
    letters.append(x)

for x in range(0, len(letters)):
    letter = letters[x]
    if letter.isupper():
        capitals.append(x)

print(capitals)
