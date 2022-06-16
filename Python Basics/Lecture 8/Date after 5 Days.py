d = int(input())
m = int(input())

days_in_month = 31

if m == 2:
    days_in_month = 28
elif m == 4 or m == 6 or m == 9 or m == 11:
    days_in_month = 30

d+=5

if d > days_in_month:
    d -= days_in_month
    m+=1
    if m > 12:
        m = 1

print("%d.%02d" % (d, m))
