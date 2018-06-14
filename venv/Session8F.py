class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

class Customer:
    def __init__(self, cid, loyaltyPoints):
        self.cid = cid
        self.loyaltyPoints = loyaltyPoints

class Employee(Person,Customer):  #IS-A Relation (Multiple)
    def __init__(self,name, age, designation, salary, cid, points):
        #super().__init__(name,age)
        Person.__init__(self,name,age)
        Customer.__init__(self,cid,points)
        self.designation = designation
        self.salary = salary


print(Person.__dict__)
print(Employee.__dict__)

e1 = Employee("John",30,"Software Engr",30000,101,220)

print(e1.__dict__)