class Student():
    sum = 0
    # name = 'qiyue'
    # age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 0
        self.__class__.sum += 1
        # print('当前学生总数为:' + str(self.__class__.sum))

    def marking(self, score):
        if score < 0:
            score = 0
        self.score = score
        print(self.name + "同学本次考试成绩为:" + str(self.score))

    def do_homework(self):
        self.do_english_homework()
        print('homework')

    def do_english_homework(self):
        print()

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)
        # print(name)


    @staticmethod
    def add(x, y):
        print(Student.sum)
        print("this is a static method")
        # print(name)


student1 = Student('石敢当', 18)
student1.marking(89)
# Student.add(1, 2)
# student1.add(1, 2)
# student1.plus_sum()
# Student.plus_sum()
# student2 = Student('喜小乐', 18)
# Student.plus_sum()
# student3 = Student('小诺', 18)
# Student.plus_sum()
# student1.do_homework()
# student2.do_homework()



# print(student1.__dict__)
# # print(Student.__dict__)
# print(student1.name)
# # print(Student.name)
