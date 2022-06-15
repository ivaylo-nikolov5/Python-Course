
n = int(input())

chr_sum = 0

for i in range(n):
    character = input()
    chr_sum += ord(character)

print(f"The sum equals: {chr_sum}")


