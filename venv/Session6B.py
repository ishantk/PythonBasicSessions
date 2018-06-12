class Student:

    def __init__(self, roll, name, age):
        self.roll = roll
        self.name = name
        self.age = age

    def show(self):
        print("{} belongs to {} and is {} years old".format(self.roll,self.name,self.age))


s1 = Student(101,"John",30)
s2 = Student(102,"Jennie",28)
s3 = Student(103,"Jack",38)
s4 = Student(104,"Jim",34)
s5 = Student(105,"Joe",30)

s1.show()

a1 = 10
a2 = 20
a3 = 30
a4 = 40
a5 = 50

# list1 = [a1,a2,a3,a4,a5]
# print(list1)

list2 = [10,20,30,40,50]


# Collection of Objects | Collection of Reference Variables which points to the Objects
# studentList1 = [s1,s2,s3,s4,s5]
# print(studentList1)

studentList2 = [Student(101,"John",30),Student(102,"Jennie",28),Student(103,"Jack",38),]
print(studentList2)

studentList3 = []
studentList3.append(Student(101,"John",30))
studentList3.append(Student(102,"Jennie",28))

print(studentList3[0])
studentList3[0].show()