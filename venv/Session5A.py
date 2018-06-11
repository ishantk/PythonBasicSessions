class User:
    #Constructor
    # 1st input i.e. self is a ref var which will hold the address of object
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


u1 = User("John Watson","+91 99999 88888","john@example.com")
u1.age = 30

u2 = User("Jennie Watson","+91 99999 77777","jennie@example.com")

print(u1.__dict__)
print(u2.__dict__)

