# 正则表达式
# JSON

import re

# a = 'C|C++|Java|C#|Python|JavaScript'
qq = 'C0C++7Java8C#9Python6JavaScript1234'

# r = re.findall("Python", a)
# r = re.findall("\d", a)
# r = re.findall("\D", a)
# print(r)

"""字符集"""
s = 'abc, acc, adc, afc, aec'

# r = re.findall('a[cf]c', s)
# r = re.findall('a[^cf]c', s)
r = re.findall('a[c-f]c', s)
print(r)

"""概括字符集"""

qq = 'python 1111\tjava&678\nphp\r___'
# r = re.findall("\d", a)
# r = re.findall("[0-9]", a)
# r = re.findall("\w", a)
# r = re.findall("[A-Za-z0-9_]", a)
# r = re.findall("\W", a)
r = re.findall("\S", qq)
print(r)

"""数量词"""

# a = 'python 1111java&678php___'
qq = 'pytho0python1pythonn2'

# r = re.findall("[a-z]{3}", a)
# r = re.findall("[a-z]{3,6}", a)
# r = re.findall("[a-z]{3,6}?", a)
# * 匹配0次或无限多次
r = re.findall("python*", qq)


# + 匹配1次或无限多次
r = re.findall("python+", qq)

# ? 匹配0次或1次
r = re.findall("python?", qq)

r = re.findall("python{1,2}?", qq)
print(r)

"""边界匹配"""

# qq = "100001"
qq = "100000001"

# r = re.findall('^\d{4,8}$', qq)
r = re.findall('000$', qq)
print(r)

"""组"""

a = 'PythonPythonPythonPythonPython'

# r = re.findall('Python', a)
r = re.findall('(Python)}{3}(JS)', a)
print(r)

""""""

lanuage = 'PythonC#JavaC#PHPC#'

def convert(value):
    matched = value.group()
    return '!!'+ matched + '!!'

# r = re.findall('c#.{1}', lanuage, re.I | re.S)
# r = re.sub('C#', 'GO', lanuage, 1)

# lanuage = lanuage.replace('C#', 'GO')
r = re.sub('C#', convert, lanuage)
# print(lanuage)
print(r)

s = 'ABC3721D86'


def convert1(value):
    matched = value.group()
    if int(matched) >= 6:
        return str(9)
    else:
        return str(0)

r = re.sub('\d', convert1, s)
print(r)

s = '8C3721D86'

r = re.match('\d', s)
print(r.span())
r1 = re.search('\d', s)
print(r1.group())
r2 = re.findall('\d', s)
print(r2)

# s = 'life is short, i use python'
s = 'life is short, i use python, i love python'

r = re.search('(life(.*)python(.*)python)', s)
print(r)
print(r.group(0))
print(r.group(1))
print(r.group(2))
# r = re.search('life(.*)python', s)
r = re.findall('life(.*)python', s)
# print(r.group(0))
print(r)