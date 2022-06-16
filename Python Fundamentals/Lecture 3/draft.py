year = int(input())

is_happy_year = False

while not is_happy_year:
    year += 1
    str_year = str(year)
    year_set = set(str(year))

    is_happy_year = len(str_year) == len(year_set)

print(year)


