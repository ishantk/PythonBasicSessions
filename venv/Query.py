#OOPS : Object is a Container and Class is also a Container

class MobilePhone:

    name = "iPhone7"
    brand = "Apple"

    # Constructor
    def __init__(self, ram, mem, col):
        self.ram = ram
        self.mem = mem
        self.color = col





# Write Operation
# 1. Create an Attribute if its not thr
# 2. Update the value if its thr

MobilePhone.screen = "5 inches"
MobilePhone.screen = "4 inches"

print(MobilePhone.name," belongs to ", MobilePhone.brand," and has a screen size of", MobilePhone.screen)

print(MobilePhone.__dict__)

# Creation of an Object
m1 = MobilePhone("4 GB","128 GB","Black")

m1.price = 60000


#Ref Variable can access the property of class if it is not thr in the object
print(m1.__dict__)
print(m1.name)

# print(MobilePhone.ram)
# Object can access Class's Property
# Class cannot access Object's Property

name = ["John","Jennie"]
if name[0].startswith("J"):
    print("Wow")