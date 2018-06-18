class Cab:
    def bookCab(self):
        print("Cab Booked..")
        pass

class MicroCab(Cab):
    def bookCab(self):
        print("Micro Cab Booked..")

class MiniCab(Cab):
    def bookCab(self):
        print("Mini Cab Booked..")

class LuxuryCab(Cab):
    def bookCab(self):
        print("Luxury Cab Booked..")


cRef = MicroCab()
cRef.bookCab()
print("=================")
cRef = MiniCab()
cRef.bookCab()
print("=================")
cRef = LuxuryCab()
cRef.bookCab()