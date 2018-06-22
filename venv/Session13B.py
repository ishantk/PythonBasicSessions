import threading
import time

lock = threading.Lock()

class Table:
    def printTable(self,num):
        lock.acquire()
        for i in range (1,11):
            time.sleep(1)
            print(num,i,"'s are ",(num*i))
        lock.release()


class MyThread(threading.Thread):

    def __init__(self,tRef):
        threading.Thread.__init__(self) # MUST Execute Parent's Constructor here
        self.tRef = tRef

    def run(self):
        self.tRef.printTable(5)

class YourThread(threading.Thread):

    def __init__(self,tRef):
        threading.Thread.__init__(self) # MUST Execute Parent's Constructor here
        self.tRef = tRef

    def run(self):
        self.tRef.printTable(7)

print("**App Started**")

t = Table()
# Printing of Table is done by main thread
#t.printTable(5)

# Printing the table of 5 is responsibility of MyThread
mRef = MyThread(t)
yRef = YourThread(t)

mRef.start()
yRef.start()

print("**App Finished**")