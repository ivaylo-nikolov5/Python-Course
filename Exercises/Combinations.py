n = int(input())

combinations_counter = 0

for i in range(0, n+1):
    for j in range(0, n+1):
        for k in range(0, n+1):
            sum = i + j + k
            if sum == n:
                combinations_counter += 1

print(combinations_counter)