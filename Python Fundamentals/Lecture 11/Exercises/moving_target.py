sequence_of_targets = list(map(int, input().split(" ")))

command = input()
while command != "End":
    explode = command.split(" ")
    action = explode[0]
    index = int(explode[1])
    value = int(explode[2])
    if action == "Shoot":
            sequence_of_targets[index] -= value
            if sequence_of_targets[index] <= 0:
                sequence_of_targets.remove(sequence_of_targets[index])
    elif action == "Add":
        sequence_of_targets[index] += value

        print(f"Invalid placement!")
    elif action == "Strike":
        for i in range(index-value, index+value+1):
            sequence_of_targets.remove(i)
            print("Strike missed!")

sequence_of_targets = str(sequence_of_targets)
print("|".join(sequence_of_targets))