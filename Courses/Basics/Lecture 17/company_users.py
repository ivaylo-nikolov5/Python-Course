def company_users():
    command = input()
    users_dict = {}
    while command != "End":
        command = command.split(" -> ")
        company = command[0]
        user = command[1]
        if company not in users_dict:
            users_dict[company] = []
        if user not in users_dict[company]:
            users_dict[company].append(user)

        command = input()

    for x in users_dict:
        print(x)
        for y in users_dict[x]:
            print(f"-- {y}")


company_users()
