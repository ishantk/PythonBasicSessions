class Person:

    def __init__(self,name,phone,age,gender,address):
        self.name = name
        self.phone = phone
        self.age = age
        self.gender = gender
        self.address = address # HAS-A Relation | 1 to 1
        print("address is",address)


    def showPerson(self):
        print("{} is {} years old and can be contacted at {}".format(self.name,self.age,self.phone))
        self.address.showAddress()


class Address:
    def __init__(self, adrsLine, city, state, zipCode):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state
        self.zipCode = zipCode

    def showAddress(self):
        print("{} is in {}".format(self.adrsLine,self.city))


a1 = Address("Country Homes","Bengaluru","Karnataka",520001)
a1.showAddress()

print("a1 is",a1)


p1 = Person("John","+91 99999 88888",30,"M",a1)
print("p1 is",p1)

p1.showPerson()