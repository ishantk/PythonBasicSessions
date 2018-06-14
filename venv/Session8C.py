class Product:

    def __init__(self,pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def __str__(self):
        data = "Product Details: {}, {}, {}".format(self.pid, self.name, self.price)
        return data


# p1 = Product(101,"LED TV",30000)
# print(p1)