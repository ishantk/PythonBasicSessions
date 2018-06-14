class Employee:

    def __init__(self, id, name, salary):
        self.id = id
        self.__name = name
        self.salary = salary

    # setter -> write the data
    def getName(self):
        return self.__name

    # getter -> read the data
    def setName(self, name):
        self.__name = name

    # deleter -> read the data
    def setName(self):
        del self.__name

    def showEmployee(self):
        print(self.id,self.name,self.salary)

    @property
    def mySalary(self):
        return self.salary

    @mysalary.setter
    def setSalary(self,salary):
        self.salary = salary

    @mysalary.getter
    def getSalary(self):
        return self.salary

    @mysalary.deleter
    def delSalary(self):
        del self.salary


eRef1 = Employee(101,"John",30000)
eRef2 = Employee(202,"Jennie",40000)

#eRef1.__name = "Wow" # this shall create a new attribute in my object

#eRef1.setName("John JJ")

#property decorator can be accessed as a property/attribute

eRef1.setSalary = 40000

print(eRef1.mySalary)

print(eRef1.__dict__)
#eRef1.__name = "John Watson"


# print(eRef1.getName())
#
# print(eRef1)
# print(eRef2)
#print(eRef1.__str__())
#print(eRef2.__repr__())

#del eRef1.id
#del eRef2.name

#del eRef1

# print(eRef1.__dict__)
# print(eRef2.__dict__)


