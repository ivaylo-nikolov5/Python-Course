number = int(input())

positive_list, count_of_positives = [], 0
negative_list, negative_sum = [], 0


for i in range(number):
    numbers = int(input())
    if numbers >= 0:
        positive_list.append(numbers)
        count_of_positives += 1
    else:
        negative_list.append(numbers)
        negative_sum += numbers
print(positive_list)
print(negative_list)
print(f"Count of positives: {count_of_positives}")
print(f"Sum of negatives: {negative_sum}")