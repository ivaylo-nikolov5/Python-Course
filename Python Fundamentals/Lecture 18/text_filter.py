def text_filter(words, text):
    for x in words:
        while x in text:
            text = text.replace(x, "*"*len(x))

    print(text)


phrases = input().split(", ")
paragraph = input()

text_filter(phrases, paragraph)