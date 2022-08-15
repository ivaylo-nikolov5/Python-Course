jobs = list(int(x) for x in input().split(", "))
idx = int(input())

cycles = 0
done = False

while True:
    min_task = min(jobs)
    for task in range(len(jobs)):
        if jobs[task] == min_task:
            cycles += jobs[task]
            jobs[task] = 99999999
            if task == idx:
                done = True
                break
    if done:
        break


print(cycles)

