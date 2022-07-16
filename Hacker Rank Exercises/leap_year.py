def is_leap(year):
    leap_year = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_year = True

    return leap_year


year = int(input())
print(is_leap(year))