class Point:

    def __init__(self, x ,y ,z):
        self.x = x
        self._y = y
        self.__z = z

    def __showPoint(self):
        pass


p1 = Point(10,20,30)
print("x is:",p1.x)
print("y is:",p1._y)
#print("z is:",p1.__z) #error
print("z is:",p1._Point__z)

print("p1 dict:",p1.__dict__)

#p1.__showPoint()      #ERROR
p1._Point__showPoint() #OK

print(Point.__dict__)