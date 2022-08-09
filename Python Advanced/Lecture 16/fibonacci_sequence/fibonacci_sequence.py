from fibonacci_sequence.fibonacci_sequence import create_sequence, find_index

command = input()
sequence = []

while command != "Stop":
    command = command.split()
    action = command[0]

    if action == "Create":
        stop_num = int(command[2])
        sequence = create_sequence(stop_num)
        print(*sequence, sep=" ")
    else:
        searched_num = int(command[1])
        print(find_index(sequence, searched_num))

    command = input()