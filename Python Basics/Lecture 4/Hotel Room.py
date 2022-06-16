month = input()
nights = int(input())

studio = 0.00
apartment = 0.00
studio_rent = 0.00
apartment_rent = 0.00

if month == "May" or month == "October":
    studio = 50.00
    apartment = 65.00
    studio_rent = studio * nights
    apartment_rent = apartment * nights
    if nights <= 7:
        studio_rent = studio_rent
        apartment_rent = apartment_rent
    elif 7 < nights <= 14:
        studio_rent = studio_rent - studio_rent * 0.05
        apartment_rent = apartment * nights
    else:
        studio_rent = studio_rent - studio_rent * 0.30
        apartment_rent = apartment_rent - apartment_rent * 0.10
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    studio_rent = studio * nights
    apartment_rent = apartment * nights
    if nights <= 14:
        studio_rent = studio_rent
        apartment_rent = apartment_rent
    else:
        studio_rent = studio_rent - studio_rent * 0.20
        apartment_rent = apartment_rent - apartment_rent * 0.10
else:
    studio = 76
    apartment = 77
    studio_rent = studio * nights
    apartment_rent = apartment * nights
    if nights <= 14:
        studio_rent = studio_rent
        apartment_rent = apartment_rent
    else:
        studio_rent = studio_rent
        apartment_rent = apartment_rent - apartment_rent * 0.10

print(f"Apartment: {apartment_rent:.2f} lv.")
print(f"Studio: {studio_rent:.2f} lv.")

