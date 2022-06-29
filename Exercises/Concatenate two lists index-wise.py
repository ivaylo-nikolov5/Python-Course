list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

zipped = [i + j for i, j in zip(list1, list2)]
print(zipped)