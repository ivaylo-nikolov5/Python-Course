input_type = input()
value1 = input()
value2 = input()

def greater_value(type, val1, val2):
    result = None
    if type == "int":
        if int(val1) >= int(val2):
            result = int(val1)
        else:
            result = int(val2)
    elif type == "char":
        if ord(val1) >= ord(val2):
            result = val1
        else:
            result = val2
    else:
        if val1 >= val2:
            result = val1
        else:
            result = val2
    return result


print(greater_value(input_type, value1, value2))

