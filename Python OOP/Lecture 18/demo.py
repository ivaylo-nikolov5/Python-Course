from time import time

def exec_time(function):
    def wrapper(*args):
        start_time = time()
        function(*args)
        end_time = time()
        elapsed_time = end_time - start_time
        return elapsed_time

    return wrapper

@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))
