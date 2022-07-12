from collections import deque

bees = deque(int(x) for x in input().split(" "))
nectars = [int(x) for x in input().split(" ")]
symbols = deque(input().split())

honey = 0

while nectars and bees:
    bee = bees[0]
    nectar = nectars[-1]
    symbol = symbols[0]

    if nectar < bee:
        nectars.pop()
    else:
        result = 0
        if symbol == "+":
            result = bee + nectar
        elif symbol == "-":
            result = bee - nectar
        elif symbol == "*":
            result = bee * nectar
        elif symbol == "/" and nectar > 0:
            result = bee / nectar

        honey += abs(result)

        bees.popleft()
        nectars.pop()
        symbols.popleft()

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")