area = int(input("Area = "))
grape_in_m2 = float(input("Grape per (1km)2 = "))
needed_l_wine = int(input("Needed wine = "))
workers = int(input("Workers = "))

total_grape = area * grape_in_m2
wine = (total_grape * 0.40) / 2.5
wine = int(wine)
if wine > needed_l_wine:
    liters_left = wine - needed_l_wine
    l_per_human = liters_left / workers
    liters_left = int(liters_left)
    l_per_human = int(l_per_human)
    print("Good harvest this year! Total wine: "+ str(wine) +" liters. " +
    str(liters_left)  + " Liters left  ->  "
    + str(l_per_human) + " liters per person" )
else:
    not_enough = needed_l_wine - wine
    not_enough = int(not_enough)
    not_enough = int(not_enough)
    print("It will be a tough winter! More " + str(not_enough)
    + " liters wine needed.")



