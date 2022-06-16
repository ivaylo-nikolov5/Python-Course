n = int(input())
m = int(input())

counter = 0

for left in range(-n, n):
    for top in range(-n, n):
        for right in range(left+1, n+1):
            for bottom in range(top+1, n+1):
                area = abs(right-left)*abs(bottom-top)

                if area >= m:
                    print(f"({left}, {top}) ({right}, {bottom}) -> {area}")

                    counter += 1

if counter == 0:
    print("No")
