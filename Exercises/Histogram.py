n = int(input())

lower_200 = 0
two_hund_to_399 = 0
four_hund_to_599 = 0
six_hund_to_899 = 0
higher_800 = 0
total = 0

for i in range(n):
    num = int(input())
    if num < 200:
        lower_200 += 1
    elif 200 <= num < 400:
        two_hund_to_399 += 1
    elif 400 <= num < 600:
        four_hund_to_599 += 1
    elif 600 <= num < 800:
        six_hund_to_899 += 1
    else:
        higher_800 += 1
    total += 1

p1 = lower_200 / total * 100
p2 = two_hund_to_399 / total * 100
p3 = four_hund_to_599 / total * 100
p4 = six_hund_to_899 / total * 100
p5 = higher_800 / total * 100

print(f"{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%\n{p4:.2f}%\n{p5:.2f}%")
