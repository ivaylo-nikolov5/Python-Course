n = int(input())

odd_sum = 0
even_sum = 0

for i in range(1, n+1):
    number = int(input())
    if i % 2 != 0:
        odd_sum += number
    else:
        even_sum += number

diff = abs(odd_sum - even_sum)

if odd_sum == even_sum:
    print(f"Yes \nSum = {odd_sum}")
else:
    print(f"No \nDiff = {diff}")