import math

hours = int(input("Hours = "))      #50
days = int(input("Days = "))        #5
workers = int(input("Workers = "))  #2

working_days = hours * (days * 0.01)
working_hours = working_days * 8
extraordinary_hours = workers * 2 * days

total_hours = working_hours + extraordinary_hours
total_hours = math.floor(total_hours)

if total_hours > hours:
    print("Yes!" + str(total_hours - hours) + " hours left.")
elif total_hours < hours:
    print("Not enough time! " + str(hours - total_hours) + " hours needed.")
