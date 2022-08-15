from collections import deque

matches = 0
males = [int(male) for male in input().split() if int(male) > 0]
females = deque(int(female) for female in input().split() if int(female) > 0)

while males and females:
    current_male = males.pop()
    current_female = females.popleft()

    if 25 % current_male == 0 and current_female == 0:
        if males:
            males.pop()
        if females:
            females.popleft()
        continue
    elif 25 % current_male == 0:
        if males:
            males.pop()
        continue
    elif 25 % current_female == 0:
        if females:
            females.popleft()
        continue

    if current_male <= 0:
        females.appendleft(current_female)
        continue
    elif current_male == current_female:
        matches += 1
    else:
        males.append(current_male - 2)

print(f"Matches: {matches}")
print(f"Males left: {'none' if not males else ', '.join(str(male) for male in reversed(males))}")
print(f"Females left: {'none' if not females else ', '.join(str(male) for male in females)}")