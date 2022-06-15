people = int(input())
wagons = list(map(int, input().split(" ")))
for i in range(len(wagons)):
    if people >= 4:
        summing = people - (people - 4) - wagons[i]
        people -= summing
        wagons[i] += summing
    else:
        wagons[i] += people
        people -= wagons[i]

if wagons.count(4) < len(wagons):
    print("The lift has empty spots!")
else:
    print(f"There isn't enough space! {people} people in a queue!")

wagons = list(map(str, wagons))
print(" ".join(wagons))

