red_cards = input().split(" ")

team_a, count_a = [], 11
team_b, count_b = [], 11
is_finished = False
for i in red_cards:
    if i in team_a or i in team_b:
        continue
    if "A" in i:
        team_a.append(i)
        count_a -= 1
    else:
        team_b.append(i)
        count_b -= 1
    if count_a <= 6 or count_b <= 6:
        is_finished = True
        break

print(f"Team A - {count_a}; Team B - {count_b}")

if is_finished:
    print("Game was terminated")


