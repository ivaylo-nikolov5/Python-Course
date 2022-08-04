import re

with open("text.txt") as file, open("output.txt", "a") as output:
    for row, line in enumerate(file):
        letters = len(re.findall(r"[a-zA-Z]", line))
        punct_marks = len(re.findall(r"[.,'!?`\-=*]", line))

        output.write(f"Line {row + 1}: -I was quick to judge him, but it wasn't his fault. ({letters})({punct_marks})\n")

