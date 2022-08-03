import os

try:
    os.remove("file_for_deleting.txt")
except FileNotFoundError:
    print("File already deleted!")