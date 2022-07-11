n = int(input())

guests = set()

for _ in range(n):
    guest = input()
    guests.add(guest)

guest = input()

while not guest == "END":
    if guest in guests:
        guests.remove(guest)
    guest = input()
     
guests = [x for x in guests]

guests = list(sorted(guests))

print(len(guests))
print(*guests, sep="\n")