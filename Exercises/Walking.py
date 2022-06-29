goal = 10000

sum_steps = 0


while sum_steps < goal:
    steps = input()
    if steps == "Going home":
        last_steps = int(input())
        sum_steps += last_steps
        break
    else:
        sum_steps += int(steps)


diff = abs(sum_steps - goal)

if goal < sum_steps:
    print(f"Goal reached! Good job!\n{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
