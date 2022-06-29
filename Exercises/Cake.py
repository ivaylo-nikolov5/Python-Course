width1 = int(input())
width2 = int(input())

pieces = width2 * width1
is_gone = False
pieces_took = input()
while pieces_took != "STOP":
    pieces_took = int(pieces_took)
    pieces -= pieces_took
    if pieces < 0:
        is_gone = True
        break
    pieces_took = input()

if not is_gone:
    print(f"{pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(pieces)} pieces more.")
