import math

tournaments = int(input())
starting_points = int(input())

total_points = starting_points
average_points = 0
wins = 0

for i in range(tournaments):
    stage = input()
    stage = stage.upper()
    if stage == "W":
        total_points += 2000
        average_points += 2000
        wins += 1
    elif stage == "F":
        total_points += 1200
        average_points += 1200
    else:
        total_points += 720
        average_points += 720

average_points = math.floor(average_points / tournaments)
wins = (wins/tournaments)*100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{wins:.2f}%")