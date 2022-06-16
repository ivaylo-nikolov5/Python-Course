meerkat = []

meerkat.append(input())
meerkat.append(input())
meerkat.append(input())

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)