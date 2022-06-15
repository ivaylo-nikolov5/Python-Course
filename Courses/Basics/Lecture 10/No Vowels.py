vowels = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]
text = input()
no_vowels_list = [ch for ch in text if ch not in vowels]

print("".join(no_vowels_list))