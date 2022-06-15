num = int(input())

for i in range(97, 97+num):
    for j in range(97, 97 + num):
        for k in range(97, 97 + num):
            print(f"{chr(i)}{chr(j)}{chr(k)}")
