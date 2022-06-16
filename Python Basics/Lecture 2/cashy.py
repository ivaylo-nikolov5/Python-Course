bitcoins = int(input("Bitcoins = "))
yuans = float(input("Yuans = "))
commission_percent = float(input("Commission in % = "))

b_levs = bitcoins * 1168
b_euros = b_levs / 1.95

y_dollars = yuans * 0.15
y_levs = y_dollars * 1.76
y_euros = y_levs / 1.95

euros = b_euros + y_euros

commission = euros * 0.01 * commission_percent

total = euros - commission

print("Euros = " + str(total))