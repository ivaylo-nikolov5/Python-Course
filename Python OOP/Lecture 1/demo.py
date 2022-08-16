num1 = input()
num2 = input()

for i in range(int(num1[0]), int(num2[0]) + 1):
    for j in range(int(num1[1]), int(num2[1]) + 1):
        for k in range(int(num1[2]), int(num2[2]) + 1):
            for l in range(int(num1[3]), int(num2[3]) + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f"{i}{j}{k}{l}")