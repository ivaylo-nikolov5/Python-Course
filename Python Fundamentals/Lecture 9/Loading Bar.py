def loading_bar(num):
    percents = int(num[0])

    if int(num) >= 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")

    elif int(num) < 100:
        print(f"{num}% [" + "%" * int(num[0]) + "." * (10 - percents) + "]")
        print("Still loading...")


number = input()

loading_bar(number)


