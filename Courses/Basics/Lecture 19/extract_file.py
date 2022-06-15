def extract_file(path):
    file = path[-1]
    file = file.split(".")
    file_name = file[0]
    file_extension = file[1]
    print(f"File name: {file_name}")
    print(f"File extension: {file_extension}")


file_path = input().split('\\')
extract_file(file_path)
