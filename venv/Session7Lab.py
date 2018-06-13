class Product:

    def __init__(self,pid,name,price):
        self.pid = pid
        self.name = name
        self.price = price

    def showProduct(self):
        print("Product Details: ",self.pid,self.name,self.price)



# IS-A Relation : Inheritance | Parent/Child Relation
class Book(Product):

    def __init__(self, isbn, author, pid, name, price):
        super().__init__(pid, name, price)
        self.isbn = isbn
        self.author = author

    def showBook(self):
        print("Book Details: ",self.isbn,self.author)

print("Product's Dict: ",Product.__dict__)
print("Book's Dict: ",Book.__dict__)

""""p1 = Product(101,"ABC",100)
b1 = Book(201,"Code in Python",500)

print(p1.__dict__)
print(b1.__dict__)

#p1.showProduct()
Product.showProduct(p1)

#b1.showProduct()
Book.showProduct(b1)

Product.showProduct(b1)"""

b1 = Book("IN0045AB","John Watson",101,"Code in Python",500)
print(b1.__dict__)