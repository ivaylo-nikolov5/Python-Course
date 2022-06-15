input_string = input().split()
required_shuffles = int(input())

first_half = []
second_half = []
output_string = []

for i in range(1, len(input_string) // 2):
    first_half.append(input_string[i])
    second_half.append(input_string[i + ((len(input_string) - 2) // 2)])

for n in range(required_shuffles):
    output_string = [item for t in list(zip(second_half, first_half)) for item in t]
    first_half.clear()
    second_half.clear()
    for m in range(len(output_string) // 2):
        first_half.append(output_string[m])
        second_half.append(output_string[m + (len(output_string) // 2)])

output_string.insert(0, input_string[0])
output_string.append(input_string[len(input_string) - 1])

print(output_string)