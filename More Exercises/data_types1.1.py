def data_types(data_type, data):
    if data_type == "int":
        return int(data) * 2

    elif data_type == "real":
        return f"{float(data) * 1.5:.2f}"

    elif data_type == "string":
        return f"${data}$"


data_type = input()
data = input()

print(data_types(data_type, data))
