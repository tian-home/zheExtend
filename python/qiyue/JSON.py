import json

# json_str = '{"name":"qiyue", "age":18}'
json_str = '[{"name":"qiyue", "age":18, "flag":false}, {"name":"qiyue", "age":18}]'

"""反序列化"""

student = json.loads(json_str)

print(student)
print(type(student))
# print(student['name'])
# print(student['age'])

"""序列化"""

student = [
            {"name":"qiyue", "age":18, "flag":False},
            {"name":"qiyue", "age":18}
          ]

json_str = json.dumps(student)
print(json_str)
print(type(json_str))