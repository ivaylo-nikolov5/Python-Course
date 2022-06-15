def capitals(country, capital):
    country_capital = dict(zip(country, capital))

    for x in country_capital:
        print(f"{x} -> {country_capital[x]}")


countries_input = input().split(", ")
capitals_input = input().split(", ")

capitals(countries_input, capitals_input)