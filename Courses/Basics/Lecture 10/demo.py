happiness = list(map(int, input().split(" ")))
a = int(input())

happiness_list = list(filter(lambda x: x >= sum(happiness) / len(happiness), happiness))

if len(happiness_list) < len(happiness) / 2:
    print(f"Score: {len(happiness_list)}/{len(happiness)}. Employees are not happy!")
else:
    print(f"Score: {len(happiness_list)}/{len(happiness)}. Employees are happy!")