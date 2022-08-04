info = []

with open("text.txt") as file, open("output.txt", "w") as output:
    counter = 1
    for line in file.readlines():
        letters = 0
        punctuation_marks = 0
        for ch in line:
            if ch.isalpha():
                letters += 1
            elif ch in "-.,?!';:`()":
                punctuation_marks += 1

        text = f"Line {counter}: {line.strip()} ({letters})({punctuation_marks})\n"
        output.writelines(text)

        counter += 1

