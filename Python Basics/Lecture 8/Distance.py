speed = int(input())
first = int(input())
second = int(input())
third = int(input())

first_hour = first / 60
second_hour = second / 60
third_hour = third / 60

distance_f_speed = speed * first_hour
ten_perc = speed + 0.1*speed
after_incr = ten_perc * second_hour
five_perc = ten_perc - ((ten_perc*5)/100)
after_decr = five_perc * third_hour

total = distance_f_speed + after_incr + after_decr

print(f"{total:.2f}")


