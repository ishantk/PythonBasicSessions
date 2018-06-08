#import Session3

a = 10
name = "John"

#MUTABLE
names = ["John","Jennie","Jim","Jack","John","Joe"]
names[1] = 100

#IMMUTABLE
moreNames = (10,20,30,20)

someNames = {"John","Jennie","Jim","Jack","John","Joe"}
allNames = {101:"John",201:"Jennie",301:"Jim",101:"Jack",501:"John",601:"Joe"}

someDict = {"auto":40,"bike":30,"mini":80,"available":False}

print(names)
print(moreNames)
print(someNames)
print(allNames)
print(someDict)

print(allNames[201])

for var in allNames:
    print(var, allNames[var])
        