import os

try:
    file_path = "my_second_file.txt"
    os.remove(file_path)
except FileNotFoundError:
    print("File already deleted!")

# ===========================================

if os.path.exists("my_second_file.txt"):
    os.remove("my_second_file.txt")
else:
    print("File already deleted!")
