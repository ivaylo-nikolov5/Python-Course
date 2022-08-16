def words_sorting(*args):
    result = ""
    sorted_words = {}
    for word in args:
        if word not in sorted_words:
            sorted_words[word] = sum([ord(ch) for ch in word])
    if sum(sorted_words.values()) % 2 == 0:
        sorted_words = sorted(sorted_words.items(), key=lambda x: x[0])
    else:
        sorted_words = sorted(sorted_words.items(), key=lambda x: -x[1])

    for word, value in dict(sorted_words).items():
        result += f"{word} - {value}\n"

    return result.strip()

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

