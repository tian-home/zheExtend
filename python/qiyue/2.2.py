total = 0
l_waka = [47, 51, 49, 50, 49, 46, 51, 48, 52, 49]


for i in l_waka:
    total = total + i

mean01 = total / len(l_waka)

total01 = 0

for i in l_waka:
    total01 = (i - mean01) **2 + total01

var = total01 / (len(l_waka) - 1)
print(total, mean01, var)