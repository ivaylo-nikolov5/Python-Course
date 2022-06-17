def int_func(data):
    return int(data) * 2


def real_func(data):
    return f"{float(data) * 1.5:.2f}"


def string_func(data):
    return f"${data}$"


def data_types(data_type, data):
    result = ""
    if data_type == "int":
        result = int_func(data)

    elif data_type == "real":
        result = real_func(data)

    elif data_type == "string":
        result = string_func(data)

    print(result)


data_type = input()
data = input()

data_types(data_type, data)
