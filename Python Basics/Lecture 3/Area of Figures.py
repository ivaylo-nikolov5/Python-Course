import math

figure = input("Please enter the name of the figure(square, rectangle, circle, triangle): ")

if figure == "square":
    a = float(input("a = "))
    s_area = a * a
    print("%.2f" % (s_area))
elif figure == "rectangle":
    a = float(input("a = "))
    b = float(input("b = "))
    r_area = a * b
    print("%.2f" % (r_area))
elif figure == "circle":
    r = float(input("r = "))
    c_area = math.pi * r * r
    print("%.2f" % (c_area))
elif figure == "triangle":
    a = float(input("a = "))
    h = float(input("b = "))
    t_area = a * h / 2
    print("%.2f" % (t_area))
else:
    print("No such figure found! Try again!")


