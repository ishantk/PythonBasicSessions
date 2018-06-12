class Student:

    college = "ABC Group"

    #Constructor
    def __init__(self,rl,nm,ag):
        self.roll = rl
        self.name = nm
        self.age = ag

    def showStudent(self):
        print("{} belongs to {}".format(self.roll,self.name))

    def showCollege():
        print("Welcome to College ",Student.college)

    @classmethod
    def showCollegeAgain(cls):
        print("Welcome to College ", cls.college)


s1 = Student(101,"John",20)
s2 = Student(102,"Jennie",22)

s1.showStudent() # -> Translated to Student.showStudent(s1)
s2.showStudent()
Student.showStudent(s1)
