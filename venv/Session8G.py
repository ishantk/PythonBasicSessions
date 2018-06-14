class Person():
    def __init__(self):
        print("Person Object Created")
    pass

class Customer:
    def __init__(self):
        print("Customer Object Created")
    pass

class Employee(Person,Customer):  #IS-A Relation (Multiple)
    def __init__(self):
        #super().__init__()
        #super(Person,self).__init__()
        #super(Customer, self).__init__()

        Person.__init__(self)
        Customer.__init__(self)

        print("Employee Object Created")


e1 = Employee()

class CA:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def fun(self):
        pass

class CB(CA):
    pass

print(CA.__dict__)
print(CB.__dict__)

cb = CB(10,20)
print(cb.__dict__)