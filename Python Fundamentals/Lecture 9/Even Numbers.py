# numbers = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(" ")))))
# print(numbers)

def evens(numbers):
    if numbers % 2 == 0:
        return True

    return False


result = filter(evens, list(map(int, input().split(" "))))
print(list(result))