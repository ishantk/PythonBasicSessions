print(__name__)


def sayHello():
    print("Hello")

def addNumbers(a, b):
    c = a+b
    print("addition is ",c)

sayHello()
addNumbers(10,20)
addNumbers(12.23,15.54)
addNumbers("John","Jennie")

def canVote(age):
    return (age>18)

if canVote(20):
    print("You can Vote")
else:
    print("You cannot Vote")


# if i pass a String line smiling to the function
# i should get back smilingly

def covertMyString(str):

    # Logic goes here


    return str
