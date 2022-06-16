w = float(input())
h = float(input())

w_to_cm = w * 100
h_to_cm = h * 100

# 120 * 12 = 1440cm       60cm ost.         w= 11 * 70 = 711cm
#mesta = 11 * 12 - 3 = 123
rows = w_to_cm//120

h_to_cm-=100


buros_in_row = h_to_cm//70
all_buros = rows * buros_in_row - 3

all_buros = int(all_buros)
print(all_buros)




