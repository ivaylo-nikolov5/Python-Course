try:
    file = open("text.txt")
    file.close()
except FileNotFoundError:
    print('File not found')


