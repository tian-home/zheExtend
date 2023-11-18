
def curve_pre():
    a = 25
    def curve(x):
        return a*x*x
    return curve

a = 10
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))

def f1():
    a = 10
    def f2():
        return a
    return f2

f = f1()
print(f.__closure__)

o = 0

# def go(step):
#     global o
#     new_pos = o + step
#     o = new_pos
#     return new_pos
#
# print(go(2))
# print(go(3))
# print(go(5))



def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go

tourist = factory(o)
print(tourist(2))
print(o)
print(tourist(3))
print(o)
print(tourist(5))
print(o)
