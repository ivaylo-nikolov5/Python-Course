import math

year_type = input()
p = int(input())
h = int(input())

result = 0
if year_type == "leap":
    weeknds_in_sofia = 48 - h
    games_w_sofia = weeknds_in_sofia * (3.0 / 4)
    games_in_born_town = h
    holiday_games = p * (2.0 / 3)
    total = games_in_born_town + games_w_sofia +holiday_games

    result = total + total * 0.15
else:
    weeknds_in_sofia = 48 - h
    games_w_sofia = weeknds_in_sofia * (3.0 / 4)
    games_in_born_town = h
    holiday_games = p * (2.0 / 3)
    total = games_in_born_town + games_w_sofia + holiday_games

    result = total

print(math.floor(result))






