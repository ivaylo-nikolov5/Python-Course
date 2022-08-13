def is_inside(r, c, rs):
    return 0 <= r < rs and 0 <= c < rs


rows = 6
points = 0

matrix = [[x for x in input().split()] for _ in range(rows)]

for attempt in range(3):
    row, col = [int(x) for x in eval(input())]

    if is_inside(row, col, rows):
        if matrix[row][col] != "B":
            continue

        matrix[row][col] = 0
        for idx in range(rows):
            points += int(matrix[idx][col])

if points >= 300:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
elif points >= 200:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif points >= 100:
    print(f"Good job! You scored {points} points, and you've won Football.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")





