class User:
    # Define Attributes Here in Class
    # Belong to Class
    name = "NA"
    phone = "NA"
    email = "NA"


u1 = User()
u2 = User()

# Write Operation
u1.name = "John"

User.company = "Auribises"

print(u1.__dict__)
print(u2.__dict__)
print(User.__dict__)

# Reference to the object can read the data(attribute) of class
print(u1.name)
print(u2.name)
print(User.name," ",User.company)

