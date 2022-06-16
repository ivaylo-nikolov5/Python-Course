def next_version(version_number):
    version_number = int("".join(version_number)) + 1
    version_number = [x for x in str(version_number)]
    print(".".join(version_number))


data = input().split(".")
next_version(data)