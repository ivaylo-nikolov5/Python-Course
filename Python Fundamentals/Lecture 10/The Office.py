happiness = input().split(" ")
happiness = list(map(int, happiness))
improvement = int(input())

happy_employees = list(filter(lambda emp: emp >= sum(happiness) / len(happiness), happiness))

if len(happy_employees) < len(happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(happiness)}. Employees are not happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(happiness)}. Employees are happy!")

