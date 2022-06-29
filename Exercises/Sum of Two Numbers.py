start = int(input())
end = int(input())
magic_number = int(input())

combinations = 0
is_found = False

for i in range(start, end+1):
    for j in range (start, end + 1):
        combinations += 1
        if i + j == magic_number:
            print(f"Combination N:{combinations} ({i} + {j} = {magic_number})")
            is_found = True
            exit(i)

if not is_found:
    print(f"{combinations} combinations - neither equals {magic_number}")
