from jc01.c6 import Human

class Student(Human):
    # sum = 0
    def __init__(self, school, name, age):
        self.school = school
        # Human.__init__(self, name, age)
        super(Student, self).__init__(name, age)
        # self.score = 0
        # self.__class__.sum += 1

    def do_homework(self):
        super(Student, self).do_homework()
        print('english homework')

student1 = Student('人民路小学', '石敢当', 18)
student1.do_homework()
# print(student1.sum)
# print(student1.name)
# print(student1.age)
# print(Student.sum)
# student1.get_name()