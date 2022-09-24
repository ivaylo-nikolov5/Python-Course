import time


def exec_time(function):
    def wrapper(*args):
        start_time = time.time()
        func_result = function(*args)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time

    return wrapper


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())


