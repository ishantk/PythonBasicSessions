class Counter:

    count1 = 0

    def __init__(self):
        self.count2 = 0

    def incrementCount(self):
        Counter.count1 = Counter.count1+1
        self.count2 = self.count2 + 1

    def showCount(self):
        print("count1 is",Counter.count1)
        print("count2 is",self.count2)

c1 = Counter()
c2 = Counter()
c3 = c1

c1.incrementCount()
c2.incrementCount()
c3.incrementCount()

c1.incrementCount()
c2.incrementCount()
c2.incrementCount()


print("---------c1---------")
               #  count1   count2
c1.showCount() #  6        3,2
print("---------c2---------")
c2.showCount() #  6        3
print("---------c3---------")
c3.showCount() #  6        3,1
