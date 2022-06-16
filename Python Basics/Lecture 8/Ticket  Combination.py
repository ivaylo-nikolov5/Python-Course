number = int(input())

passed_combinations = 0

for sym_1 in range(66, 77):
    for sym_2 in range(102, 96, -1):
        for sym_3 in range(65, 68):
            for sym_4 in range(1, 11):
                for sym_5 in range(10, 0, -1):
                    if sym_1 % 2 == 0:
                        passed_combinations += sym_1 + sym_2 + sym_3 +sym_4 + sym_5

