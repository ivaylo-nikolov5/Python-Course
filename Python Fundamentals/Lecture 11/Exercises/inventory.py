def collect_func(items: list, thing):
    if thing not in items:
        items.append(thing)


def drop_func(items: list, thing):
    if thing in items:
        items.remove(thing)


def combine_func(items: list, thing):
    explode = thing.split(":")
    if explode[0] in items:
        items.insert(items.index(explode[0]) + 1, explode[1])


def renew_func(items: list, thing):
    if thing in items:
        items.remove(thing)
        items.append(thing)


def inventory(tools):
    command = input()
    while command != "Craft!":
        explode = command.split(" - ")
        action = explode[0]
        tool = explode[1]
        if action == "Collect":
            collect_func(tools, tool)
        elif action == "Drop":
            drop_func(tools, tool)
        elif action == "Combine Items":
            combine_func(tools, tool)
        elif action == "Renew":
            renew_func(tools, tool)

        command = input()
    print(", ".join(tools))


things = input().split(", ")
inventory(things)
