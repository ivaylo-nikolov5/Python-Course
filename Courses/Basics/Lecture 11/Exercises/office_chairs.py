def office_chairs(rooms):

    left_chairs = 0
    is_okay = True

    for i in range(1,  rooms + 1):

        chairs = input()
        explode = chairs.split(" ")
        free_chairs = len(explode[0])
        visitors = int(explode[1])
        needed_chairs = visitors - free_chairs

        if free_chairs < visitors:
            print(f"{needed_chairs} more chairs needed in room {i}")
            is_okay = False

        else:
            left_chairs += free_chairs - visitors

    if is_okay:
        print(f"Game On, {left_chairs} free chairs left")


office_chairs(rooms=int(input()))