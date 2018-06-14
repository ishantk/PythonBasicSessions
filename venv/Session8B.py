class Student:

    def __init__(self,roll, name, gender):
        self.roll = roll
        self.name = name
        self.gender = gender

    def __str__(self):
        message = "Welcome {}, {}, {}".format(self.roll,self.name,self.gender)
        return message

    # def __repr__(self):
    #     message = "Welcome {}, {}, {}".format(self.roll, self.name, self.gender)
    #     return message


s1 = Student(101,"John","Male")
#print(s1.__repr__())

print(s1.__repr__())
print(s1.__str__()) #__str__() will internally call __repr__()
print(s1.__dict__)