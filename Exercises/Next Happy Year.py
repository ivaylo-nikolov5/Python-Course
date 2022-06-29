year = int(input())

is_year_happy = False

while not is_year_happy:
    year += 1
    str_year = str(year)
    set_year = set(str_year)

    is_year_happy = len(str_year) == len(set_year)

print(year)