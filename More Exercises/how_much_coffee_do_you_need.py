command = input()
coffee = 0
extra_sleep = False
activities = ["coding", "dog", "cat", "movie"]

while command != "END":
    if command.isupper() and command.lower() in activities:
        coffee += 2
    elif command.islower() and command in activities:
        coffee += 1

    if coffee >= 5:
        print("You need extra sleep")
        extra_sleep = True
        break

    command = input()

if not extra_sleep:
    print(coffee)