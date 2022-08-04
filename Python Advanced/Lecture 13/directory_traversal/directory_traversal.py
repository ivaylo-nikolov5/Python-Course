from os import listdir, path

files = dict()


def traverse_dir(current_path):
    for el in listdir(current_path):
        if path.isdir(path.join(current_path, el)):
            traverse_dir(path.join(current_path, el))
        else:
            _, ext = el.split(".")
            if ext not in files:
                files[ext] = []
            files[ext].append(el)

    return files


files = traverse_dir(".")

files = dict(sorted(files.items(), key=lambda kvpt: kvpt[0]))

with open("report.txt", "w") as report:
    for file, occ in files.items():
        report.write(f".{file}\n")
        for el in occ:
            report.write(f"- - - {el}\n")