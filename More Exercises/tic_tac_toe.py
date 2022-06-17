def tic_tac_toe(one, two, three):
    if one.count(one[0]) == 3 or two.count(two[0]) == 3 or three.count(three[0]) == 3:
        if one[0] == "1" and one[1] == "1" and one[2] == "1":
            print("First player won")
        elif two[0] == "1" and two[1] == "1" and two[2] == "1":
            print("First player won")
        elif three[0] == "1" and three[1] == "1" and three[2] == "1":
            print("First player won")
        else:
            print("Second player won")
    elif one[0] == two[0] and two[0] == three[0] or one[1] == two[1] and two[1] == three[1] or one[2] == two[2] and two[2] == three[2]:
        if one[0] == "1" and two[0] == "1" and three[0] == "1":
            print("First player won")
        elif one[1] == "1" and two[1] == "1" and three[1] == "1":
            print("First player won")
        elif one[2] == "1" and two[2] == "1" and three[2] == "1":
            print("First player won")
        else:
            print("Second player won")
    elif one[0] == two[1] and two[1] == three[2] or one[2] == two[1] and two[1] == three[0]:
        if one[0] == "1" and two[1] == "1" and three[2] == "1":
            print("First player won")
        elif one[2] == "1" and two[1] == "1" and three[0] == "1":
            print("First player won")
        else:
            print("Second player won")
    else:
        print("Draw!")


first_line = input().split(" ")
second_line = input().split(" ")
third_line = input().split(" ")

tic_tac_toe(first_line, second_line, third_line)
