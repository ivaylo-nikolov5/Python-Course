number_of_snowballs = int(input())

highest_value = 0
best_snowball_data = ""
for snowballs in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if value > highest_value:
        highest_value = value
        best_snowball_data = f"{weight} : {time} = {int(highest_value)} ({quality})"

print(best_snowball_data)
