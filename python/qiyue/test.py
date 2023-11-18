a = 1.2346

# result = round(a, 2)
# print(result)


# def add(num1, num2):
#     result = num1 + num2
#     return result
#
# result = add(1, 2)
# print(result)

# def damage(skill1, skill2):
#     damage1 = skill1 * 3
#     damage2 = skill2 * 2 + 10
#     return damage1, damage2
#
# skill1_damage, skill2_damage = damage(3, 6)
# print(skill1_damage, skill2_damage)

def print_students_files(name, gender='男', age=18, college="人民路小学"):
    print('我叫'+ name)
    print('我今年' + str(age) + '岁')
    print('我是' + gender + '生')
    print('我在' + college + '上学')

print_students_files('鸡小萌', "男", 18, '人民路小学')
print("~~~~~~~~~~~~~~")
print_students_files('鸡小萌')
print("~~~~~~~~~~~~~~")
print_students_files('石敢当')
print("~~~~~~~~~~~~~~")
print_students_files('喜小乐')

# def demo(*param):
#     print(param)
#     print(type(param))

def demo(param1, *param, param2=2):
    print(param1)
    print(param)
    print(param2)

# a = (1, 2, 3, 4, 5, 6)
# demo(*a)

demo('a', 1,2,3, param2 = 'param')

def squsum(*param):
    sum = 0
    for i in param:
        sum += i*i
    print(sum)

squsum(1, 2, 3, 4, 5, 6)

def city_temp(param1, **param):
    print(param1)
    print(param)
    for key,value in param.items():
        print(key, ":", value)

a = {'bj': "32c", 'sh': '31c'}
city_temp(1)

c = 50
# def add(x, y):
#     c = x + y
#     print(c)
#
# add(1, 2)
# print(c)

def demo():
    c = 50
    for i in range(0, 9):
        a = "a"
        c += 1
    print(c)
    print(a)

# print(c)+

def func1():
    c = 2
    def func2():
        c = 3
        print(c)
    func2()

func1()


def demo():
    global c
    c = 2

demo()
print(c)

