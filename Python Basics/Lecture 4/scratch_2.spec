total_exam_min = exam_hours * 60 + exam_minutes
total_arrival_min = arrival_hours * 60 + arrival_minutes
hours_left = 0
min_left = 0

diff = abs(total_exam_min - total_arrival_min)

if total_arrival_min > total_exam_min:
    print("Late")
    if diff >= 60:
        hours_left = diff // 60
        min_left = diff % 60
        if min_left < 10:
            print(f"{hours_left}:0{min_left} hours after the start")
        else:
            print(f"{hours_left}:{min_left} hours after the start")
    else:
        if diff < 10:
            print(f"0{diff} minutes after the start")
        else:
            print(f"{diff} minutes after the start")
elif total_arrival_min == total_exam_min:
    print("On time")

elif total_arrival_min < total_exam_min:
    if diff <= 30:
        print("On time")
        print(f"{diff} minutes before the start")
    else:
        if diff >= 60:
            hours_left = diff // 60
            min_left = diff % 60
            if min_left < 10:
                print("Early")
                print(f"{hours_left}:0{min_left} hours before the start")
            else:
                print("Early")
                print(f"{hours_left}:{min_left} hours before the start")
        else:
            print("Early")
            print(f"{diff} minutes before the start")


