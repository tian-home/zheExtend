

list_x = [1, 0, 1, 1, 0, 1]
list_u = ["a", "L", "Q", "o"]
# r = filter(lambda x: True if x==1 else False, list_x)
r = filter(lambda x: True if x.lower()==x else False, list_u)
print(list(r))