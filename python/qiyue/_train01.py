import math


# def func(l_nums):
#     total = 0
#     for i in l_nums:
#         total = i + total
#     mean01 = total / len(l_nums)
#     return total, mean01
#
# result = func([1, 5, 6, 2])
# print(result)
# print(result[0], result[1])
#
# total = 0
#
# for i in range(1, 1001):
#     if i % 2 == 1:
#         total = total + i
#
# print(total)

l_nums = [568, 530, 581, 554, 536, 518, 564, 552]
total = 0
for i in l_nums:
    total += i

mean = total / len(l_nums)
total01 = 0
for i in l_nums:
    total01 += (i - mean) ** 2

var = total01 / (len(l_nums)-1)
std = math.sqrt(var / len(l_nums))
conf01 = mean - 2.365 * std
conf02 = mean + 2.365 * std

print(conf01, conf02)
