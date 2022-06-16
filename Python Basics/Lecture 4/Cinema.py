projection_type = input("Projection type?: ")
rows = int(input("Rows = "))
columns = int(input("Columns = "))

result = 0

if projection_type == "Premiere":
    result = 12 * rows * columns
elif projection_type == "Normal":
    result = 7.5 * rows * columns
else:
    result = 5 * rows * columns

print(("{:.2f} leva".format(result)))