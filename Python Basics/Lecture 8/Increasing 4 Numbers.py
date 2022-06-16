a = int(input())
b = int(input())

counter = 0

for i in range(a, b+1):
    for j in range(i+1, b+1):
        for k in range(j+1, b+1):
            for l in range(k+1, b+1):
                print(i, j, k, l)
                counter += 1
if counter == 0:
    print("No")