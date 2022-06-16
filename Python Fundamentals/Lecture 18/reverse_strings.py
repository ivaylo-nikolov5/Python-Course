def reverse_strings():
    command = input()
    while command != "end":
        reverse = list(reversed(command))
        print(f"{command} = {''.join(reverse)}")

        command = input()


reverse_strings()


#or


command = input()

while command != "end":
    reverse = command[::-1]
    print(f"{command} = {reverse}")

    command = input()