import time


def print_current_time(func):
    print(time.time())
    func()


# print_current_time(f1)
# print_current_time(f2)

def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)

    return wrapper


@decorator
def f1(func_name):
    print('This is a function' + func_name)


@decorator
def f2(func_name1, func_name2):
    print('This is a function' + func_name1)
    print('This is a function' + func_name2)


# @decorator
def f3(func_name1, func_name2, **kw):
    print('This is a function' + func_name1)
    print('This is a function' + func_name2)


f1(' test func')
f2(' test func1', 'test func2')
f2(' test func1', 'test func2', a=1, b=2, c='123')
# f = decorator(f1)
# f()
