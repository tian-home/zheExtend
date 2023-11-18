import math
# 计算一个数值列表的合计，均值，方差，标准差
total = 0
l_nums = [1, 5, 8, 3]

for i in l_nums:
    total = total + i


mean01 = total / len(l_nums)

total01 = 0

for i in l_nums:
    tmp = ((i - mean01) ** 2)
    total01 = total01 + tmp

var01 = total01 / len(l_nums)
std01 = math.sqrt(var01)
print(total, mean01, total01, var01, std01)

