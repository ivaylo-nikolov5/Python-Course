def shoot(targets):
    shot = input()
    counter = 0
    while shot != "End":
        shot = int(shot)
        if shot < len(targets) and targets[shot] != -1:
            for i in range(len(targets)):
                if targets[i] != -1 and targets[i] < targets[shot]:
                    targets[i] += targets[shot]

                elif targets[i] != -1 and targets[i] > targets[shot]:
                    targets[i] -= targets[shot]

            targets[shot] = -1
        shot = input()

    minus_one_count = targets.count(-1)
    print(f"Shot targets: {minus_one_count} ->", *targets, sep=" ")


nums = list(map(int, input().split(" ")))
shoot(nums)
