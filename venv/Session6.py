class Student:

    collegeName = "ABC Group"

    # Constructor
    def __init__(self, roll, name, age):
        self.roll = roll
        self.name = name
        self.age = age

    """def __init__(self, roll, name, age, gender):
        self.roll = roll
        self.name = name
        self.age = age
        self.gender = gender

    def __init__(self):
        pass
    """

    def showStudent(self):
        print(self.name," is ",self.age," years old")

    @classmethod
    def showCollege(cls):
        print("College is ",cls.collegeName)

    # def showCollege(self):
    #     print(self.name,"studies in ",Student.collegeName)

    # is class's method
    @staticmethod
    def show():
        print("Hello form Show and college is ",Student.collegeName)


    # acting as constructor
    @classmethod
    def createStudent(cls,rl,nm,ag):
        return cls(rl,nm,ag) #-> will execute __init__() method and create Object

#s1 = Student()

#s1 = Student()
s1 = Student(101,"John",30) #Object Construction Statement
s2 = Student(201,"Jennie",28)

#s1.showStudent() # -> Student.showStudent(s1)
Student.showStudent(s1)
s2.showStudent()

#Student.showCollege()
s1.showCollege()


def hello():
    print("This is Awesome")

hello()

s1.show()
Student.show()


s3 = Student.createStudent(301,"Jack",32)