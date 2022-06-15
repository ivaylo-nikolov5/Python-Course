def heart_delivery(data):
    current_index = 0
    last_position = 0
    while True:
        command = input().split(" ")
        if command[0] == "Love!":
            break

        index = int(command[1]) + current_index

        if index >= len(data):
            index = 0

        if -1 < index <= len(data):
            if data[index] > 0:
                data[index] -= 2
                if data[index] == 0:
                    print(f"Place {index} has Valentine's day.")

            else:
                print(f"Place {index} already had Valentine's day.")
        current_index = index
        last_position = index
    print(f"Cupid's last position was {last_position}.")
    if data.count(0) != len(data):
        print(f"Cupid has failed {len(data) - data.count(0)} places.")
    else:
        print("Mission was successful.")


nums = list(map(int, input().split("@")))
heart_delivery(nums)