exam_hours = int(input())
exam_minutes = int(input())
arrive_hours = int(input())
arrive_minutes = int(input())

late = "Late"
on_time = "On time"
early = "Early"

exam_time = (exam_hours * 60) + exam_minutes
arrive_minutes = (arrive_hours * 60) + arrive_minutes

minute_difference = arrive_minutes - exam_minutes

student_arrival = late
if minute_difference < - 30:
    student_arrival = early
elif student_arrival <= str(0):
    student_arrival = on_time
result = ""

if minute_difference != 0:
    hours_difference = abs(minute_difference) // 60
    minutes_difference = abs(minute_difference) % 60

    if hours_difference > 0:
        result = f"{hours_difference}:{minutes_difference:02} hours"
    else:
        result = f"{minutes_difference} minutes"
    if minute_difference < 0:
        result += " before the start"
    else:
        result += " after the start"

print(student_arrival)
if result:
    print(result)


