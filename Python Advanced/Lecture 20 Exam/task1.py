from collections import deque


def check_word(letters, words):
    for word in words:
        word_found = True
        for ch in word:
            if ch in letters:
                continue
            word_found = False

        if word_found:
            return word

    return ""


def is_inside(words, letter, letters):
    inside = False
    for word in words:
        if letter in word:
            letters += letter
            inside = True
            break

    return letters, inside


words = ["rose", "tulip", "lotus", "daffodil"]
letters = ""
found_word = ""
vowels_collection = deque(x for x in input().split())
consonants_collection = list(x for x in input().split())

while vowels_collection and consonants_collection:
    vowel = vowels_collection.popleft()
    consonant = consonants_collection.pop()

    letters += vowel + consonant

    if check_word(letters, words):
        found_word = check_word(letters, words)
        break

if found_word != "":
    print(f"Word found: {found_word}")
else:
    print(f"Cannot find any word!")

if vowels_collection:
    print(f"Vowels left: {' '.join(ch for ch in vowels_collection)}")

if consonants_collection:
    print(f"Consonants left: {' '.join(ch for ch in consonants_collection)}")