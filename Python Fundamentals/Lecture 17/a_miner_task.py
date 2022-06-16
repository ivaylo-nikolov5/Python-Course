def miner_task():
    command = input()
    resources = {}

    while command != "stop":
        quantity = int(input())
        if command not in resources:
            resources[command] = quantity

        else:
            resources[command] += quantity

        command = input()

    for resource in resources:
        print(f"{resource} -> {resources[resource]}")


miner_task()