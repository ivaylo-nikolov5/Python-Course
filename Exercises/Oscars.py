name = input()
academy_points = float(input())
jury = int(input())

total_points = academy_points
needed_points = 1250.5

for i in range(jury):
    evaluating = input()
    points = float(input())
    total_points += len(evaluating)*points/2
    if total_points >= needed_points:
        break

left_points = needed_points - total_points

if needed_points > total_points:
    print(f"Sorry, {name} you need {left_points:.1f} more!")
else:
    print(f"Congratulations, {name} got a nominee for leading role with {total_points:.1f}!")
