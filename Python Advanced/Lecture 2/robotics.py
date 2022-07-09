from collections import deque


def convert_str_to_seconds(str_time):
    hours, minutes, seconds = [int(x) for x in str_time.split(":")]
    return hours * 60 * 60 + minutes * 60 + seconds


def convert_seconds_to_str_time(seconds):
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // (60 * 60)
    seconds %= (60 * 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

robots = input().split(";")
process_time_by_robot = {}
busy_time_by_robot = {}

for robot in robots:
    name, process_time = robot.split("-")
    process_time_by_robot[name] = int(process_time)
    busy_time_by_robot[name] = -1


time = convert_str_to_seconds(input())

items = deque()

item = input()
while item != "End":
    items.append(item)

    item = input()

while items:
    time += 1
    time %= 24 * 60 * 60
    item = items.popleft()

    for name, busy_until in busy_time_by_robot.items():
        if time >= busy_until:
            busy_time_by_robot[name] = time + process_time_by_robot[name]
            print(f"{name} - {item} [{convert_seconds_to_str_time(time)}]")
            break
    else:
        items.append(item)