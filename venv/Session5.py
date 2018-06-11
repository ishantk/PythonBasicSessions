# Textually Represent the Object

class User:
    pass


#Object Construction Statement
#u1 is a reference variable which will point to the object
u1 = User()
u2 = User()

# Reference Copy
u3 = u1

#Write Operation

u1.name = "John Watson"
u1.phone = "+91 99999 88888"
u1.email = "john@example.com"
u1.age = 30
u1.gender = "M"
u1.address = "Redwood Shores"

u2.name = "Jennie Watson"
u2.phone = "+91 99999 77777"
u2.email = "jennie@example.com"
u2.age = 20
u2.gender = "F"
u2.address = "Country Homes"
u2.qualification = "MS"



# print(u1)
# print(u2)
# print(u3)

# Read Operation

# print(u1.__dict__)
# print(u3.__dict__)
# print(u2.__dict__)

print(u1.name,"lives in ",u1.address)
print(u2.name,"lives in ",u2.address," and is ",u2.qualification)

print("{} lives in {}".format(u1.name,u1.address))