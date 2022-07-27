def sorting_cheeses(**kwargs):
    kwargs = dict(sorted(kwargs.items(), key=lambda x: x))
    kwargs = dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
    result = ""
    for el in kwargs:
        result += f"{el}\n"
        kwargs[el] = list(sorted(kwargs[el], reverse=True))
        for val in kwargs[el]:
            result += f"{val}\n"

    return result


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
