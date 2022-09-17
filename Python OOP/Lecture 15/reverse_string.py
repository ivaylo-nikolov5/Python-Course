def reverse_text(string):
    for ch in string[::-1]:
        yield ch

for char in reverse_text("step"):
    print(char, end='')
