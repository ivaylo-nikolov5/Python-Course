cmd = input()

todo = ["" for i in range(11)]

while cmd != "End":
    explode = cmd.split("-")
    position = int(explode[0])
    note = explode[1]
    todo[position] = note

    cmd = input()

final_todo = [task for task in todo if task != ""]

print(final_todo)
