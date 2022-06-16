first = int(input())
second = int(input())
third = int(input())

total = first + second + third

minutes = total // 60
seconds = total % 60

if seconds < 10:
    print(str(minutes)+":0"+str(seconds))
else:
    print(str(minutes)+":"+str(seconds))