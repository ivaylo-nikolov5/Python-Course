chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

tot_amount_of_flowers = chrysanthemums + tulips + roses
chrysanthemum_spring_summer_price = 2
chrysanthemum_autumn_winter_price = 3.75
rose_spring_summer_price = 4.1
rose_autumn_winter_price = 4.5
tulip_spring_summer_price = 2.5
tulip_autumn_winter_price = 4.15

price_inc_perc = 0.15

total = 0

if season == "Spring" or season == "Summer":
    chrys_price = chrysanthemum_spring_summer_price * chrysanthemums
    roses_price = rose_spring_summer_price * roses
    tulips_price = tulip_spring_summer_price * tulips
else:
    chrys_price = chrysanthemum_autumn_winter_price * chrysanthemums
    roses_price = rose_autumn_winter_price * roses
    tulips_price = tulip_autumn_winter_price * tulips

total = chrys_price + roses_price + tulips_price


if holiday == "Y":
    total = total + (price_inc_perc * total)


if roses >= 7 and season == "Spring":
    total = total - (total * 0.05)
elif roses >= 10 and season == "Winter":
    total = total - (total * 0.1)


if tot_amount_of_flowers >= 20:
    total = total - (total*0.2)

print(f"{2 + total:.2f}")




