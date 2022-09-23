def type_check(var_type):
    def decorator(function):
        def wrapper(var):
            if not isinstance(var, var_type):
                return "Bad Type"
            result = function(var)
            return result

        return wrapper

    return decorator



@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

