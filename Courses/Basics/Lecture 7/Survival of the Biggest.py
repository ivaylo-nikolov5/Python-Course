integers = input().split(" ")
integers_copy = list(map(int, integers))
num = int(input())

for i in range(num):
    current_min = min(integers_copy)
    integers.remove(str(current_min))
    integers_copy.remove(current_min)

print(", ".join(integers))


