from collections import deque

quantity = int(input())
line = deque()
kid = input()

while not kid == "Start":
    line.append(kid)

    kid = input()

command = input()

while not command == "End":
    command = command.split(" ")
    if command[0] == "refill":
        quantity += int(command[1])
    else:
        command = int(command[0])
        if command <= quantity:
            print(f"{line.popleft()} got water")
            quantity -= command
        else:
            print(f"{line.popleft()} must wait")

    command = input()

print(f"{quantity} liters left")
