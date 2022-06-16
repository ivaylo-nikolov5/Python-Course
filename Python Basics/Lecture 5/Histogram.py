n = int(input())

p1=0
p2=0
p3=0
p4=0
p5=0

for i in range(1, n+1):
    current_number = float(input())
    if current_number < 200:
        p1+=1
    elif current_number >= 200 and current_number < 400:
        p2+=1
    elif current_number >= 400 and current_number < 600:
        p3+=1
    elif current_number >= 600 and current_number < 800:
        p4+=1
    else:
        p5+=1

p1_per = p1/n *100
p2_per = p2/n *100
p3_per = p3/n *100
p4_per = p4/n *100
p5_per = p5/n *100

ps = p1_per, p2_per, p3_per, p4_per, p5_per

for p in ps:
    print(f"{p:.2f}%")


