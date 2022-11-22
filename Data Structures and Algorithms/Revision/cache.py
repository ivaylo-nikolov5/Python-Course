def recursive_array_sum(array, idx):
    result = 0

    if idx == len(array):
        return result

    return array[idx] + recursive_array_sum(array, idx + 1)


array = [int(num) for num in input().split()]

array_sum = recursive_array_sum(array, 0)
print(array_sum)


array_sum = 0

while array:
    array_sum += array.pop()

print(array_sum)


# ---------------------------------------------------------------------------------------------------------


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


number = int(input())

print(factorial(number))


factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print(factorial)


# -----------------------------------------------------------------------------


def recursive_drawing(idx):
    if idx < 1:
        return

    print("*" * idx)

    recursive_drawing(idx - 1)

    print("#" * idx)


number = int(input())

recursive_drawing(number)

number = int(input())

temp = number

while temp > 0:
    print("*" * temp)
    temp -= 1

temp += 1

while temp <= number:
    print("#" * temp)
    temp += 1

# ----------------------------------------------------------------------------------------------------


def generate_vectors(number, idx, result):
    if len(result) == number:
        print(*result, sep="")
        return

    for idx in range(2):
        result.append(idx)
        generate_vectors(number, idx, result)
        result.pop()


number = int(input())

generate_vectors(number, 0, [])


# -----------------------------------------------------------------------------------------------


def is_inside(row, col, rows, cols):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return False
    return True


def find_paths(row, col, rows, cols, matrix, path, direction):
    if not is_inside(row, col, rows, cols):
        return
    elif matrix[row][col] == "*" or matrix[row][col] == "v":
        return
    elif matrix[row][col] == "e":
        path.append(direction)
        print(*path, sep="")
        path.pop()
        return

    path.append(direction)
    matrix[row][col] = "v"

    find_paths(row, col + 1, rows, cols, matrix, path, "R")
    find_paths(row + 1, col, rows, cols, matrix, path, "D")
    find_paths(row, col - 1, rows, cols, matrix, path, "L")
    find_paths(row - 1, col, rows, cols, matrix, path, "U")

    matrix[row][col] = "-"
    path.pop()


rows = int(input())
cols = int(input())

matrix = []
for _ in range(rows):
    row = input()
    matrix.append([x for x in row])

find_paths(0, 0, rows, cols, matrix, [], "")


# ----------------------------------------------------------------------------------------------------




