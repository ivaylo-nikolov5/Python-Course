tail, body, head = input(), input(), input()

animal = [tail, body, head]
meerkat = animal[0], animal[2] = animal[2], animal[0]

print(animal)