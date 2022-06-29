movie = input()
student = 0
standard = 0
kid = 0

total = 0
is_done = False

while movie != "Finish":
    seats = int(input())
    sold_tickets = 0
    total_places = seats
    while total_places > 0:
        ticket = input()
        if ticket == "End":
            break

        if ticket == "Finish":
            is_done = True
            break

        if ticket == "student":
            student += 1
            total += 1
            sold_tickets += 1
        elif ticket == "standard":
            standard += 1
            total += 1
            sold_tickets += 1
        else:
            kid += 1
            total += 1
            sold_tickets += 1

        total_places -= 1

    print(f"{movie} - {sold_tickets/seats*100:.2f}% full.")


    if is_done:
        break
    movie = input()




print(f"Total tickets: {total}")
print(f"{student / total * 100:.2f}% student tickets.")
print(f"{standard / total * 100:.2f}% standard tickets.")
print(f"{kid / total * 100:.2f}% kids tickets.")
