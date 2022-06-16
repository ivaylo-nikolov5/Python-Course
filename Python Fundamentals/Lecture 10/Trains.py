wagons = int(input())
train = [0 for x in range(wagons)]

splitting = input()
while splitting != "End":
    splitting = splitting.split(" ")
    command = splitting[0]
    if command == "add":
        people = int(splitting[1])
        train[-1] += people
    elif command == "insert":
        index = int(splitting[1])
        people = int(splitting[2])
        train[index] += people
    elif command == "leave":
        index = int(splitting[1])
        people = int(splitting[2])
        train[index] -= people

    splitting = input()

print(train)



