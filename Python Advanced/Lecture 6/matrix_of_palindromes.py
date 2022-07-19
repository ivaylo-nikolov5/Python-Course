rows, cols = [int(x) for x in input().split()]

letters = "abcdefghijklmnopqrstuvwxyz"

for row in range(rows):
    for col in range(cols):
        print(f"{letters[row]}{letters[row + col]}{letters[row]}", end=" ")
    print()

