import threading
import time

"""class MyTask:

    def executeTask(self):
        for i in range (1,11):
            print("**MyTask**",i)"""


# IS-A Relation
class MyTask(threading.Thread):

    def run(self):
        for i in range(1, 11):
            time.sleep(1)
            print("**MyTask**", i)


#Job1
print("==Main App Started==")

# Job n is a blocker Job since it will block the jobs below
mRef = MyTask()
#mRef.executeTask()
mRef.start()

#Job2
for i in range(1,11):
    time.sleep(2)
    print("==Main==",i)

#Job3
print("==Main App Finished==")