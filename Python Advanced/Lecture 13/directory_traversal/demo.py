from os import listdir, path

files = dict()


def directory_traversal(file_path):

    for file in listdir(file_path):
        if path.isdir(path.join(file_path, file)):
            directory_traversal(path.join(file_path, file))
        else:
            _, ext = file.split(".")
            if ext not in files:
                files[ext] = []

            files[ext].append(file)

    return files


files = directory_traversal(".")
files = dict(sorted(files.items(), key=lambda kvpt: kvpt[0]))

with open("report.txt", "w") as file:
    for ext in files:
        file.write(f".{ext}\n")
        for el in files[ext]:
            file.write(f"- - - {el}\n")



