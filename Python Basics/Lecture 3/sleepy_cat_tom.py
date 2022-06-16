
rest_days = int(input())

minutes_for_playing = rest_days * 127
working_days = 365 - rest_days
minutes_for_playing_in_w_days = working_days * 63

real_playing_time = minutes_for_playing_in_w_days + minutes_for_playing

if real_playing_time < 30000:
    print("Tom sleeps well")
else:
    print("Tom will run away")

if real_playing_time < 30000:
    min_less_for_play = 30000 - real_playing_time
    new_hours = min_less_for_play / 60
    new_minutes = min_less_for_play % 60
else:
    min_more_for_play = real_playing_time - 30000
    new_hours = min_more_for_play / 60
    new_minutes = min_more_for_play % 60


new_hours = int(new_hours)
new_minutes = int(new_minutes)

if real_playing_time < 30000:
    print(str(new_hours)+" hours and "+str(new_minutes)+" less minutes for playing")
else:
    print(str(new_hours)+" and "+str(new_minutes)+" more minutes for playing")