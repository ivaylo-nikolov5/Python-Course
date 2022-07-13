from collections import deque

bees = deque(int(x) for x in input().split(" "))
nectars = [int(x) for x in input().split(" ")]
operators = deque(input().split())

honey = 0

while bees and nectars:
    bee = bees[0]
    nectar = nectars.pop()

    if nectar >= bee:
        operator = operators.popleft()
        bees.popleft()
        result = 0
        if operator == "+":
            result = bee + nectar
        elif operator == "-":
            result = bee - nectar
        elif operator == "*":
            result = bee * nectar
        elif operator == "/" and bee != 0 and nectar != 0:
            result = bee / nectar

        honey += abs(result)

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")
