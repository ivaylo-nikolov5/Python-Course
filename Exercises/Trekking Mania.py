groups = int(input())

to_5_ppl = 0
six_to_12_ppl = 0
thrteen_to_25_ppl = 0
twsix_to_40_ppl = 0
more_than_fourty = 0
total_people = 0

for i in range(groups):
    people = int(input())
    total_people += people
    if people <= 5:
        to_5_ppl += people
    elif 6 <= people <= 12:
        six_to_12_ppl += people
    elif 13 <= people <= 25:
        thrteen_to_25_ppl += people
    elif 26 <= people <= 40:
        twsix_to_40_ppl += people
    else:
        more_than_fourty += people

musala = to_5_ppl / total_people * 100
monblan = six_to_12_ppl / total_people * 100
kilimanjaro = thrteen_to_25_ppl / total_people * 100
k2 = twsix_to_40_ppl / total_people * 100
everest = more_than_fourty / total_people * 100

print(f"{musala:.2f}%\n{monblan:.2f}%\n{kilimanjaro:.2f}%\n{k2:.2f}%\n{everest:.2f}%")


