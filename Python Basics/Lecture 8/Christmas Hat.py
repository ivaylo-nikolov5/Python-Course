n = int(input())
dots = (n*2)-1
stars = 4*n +1
print("."*dots+"/|\\"+"."*dots)
print("."*dots+"\\|/"+"."*dots)

for row in range(0, n * 2):
    print("." * (dots - row) + "*" + "-" * row+"*"+"-" * row+"*"+"." * (dots - row))

print("*"*stars)
print("*"+".*"* 2*n)
print("*"*stars)
