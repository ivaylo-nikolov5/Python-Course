from fibonacci_sequence.demo import create_sequence, locate_num

sequence = []
command = input()

while command != "Stop":
    command = command.split()
    action = command[0]

    if action == "Create":
        num = int(command[2])
        sequence = create_sequence(num)
        print(*sequence, sep=" ")
    else:
        num = int(command[1])
        print(locate_num(sequence, num))

    command = input()