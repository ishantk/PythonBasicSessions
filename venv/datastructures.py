names = ["john","jennie","jim","jack","joe"]
print(names)

#refernce copy
moreName = names

print(type(names))
print(id(names))
print(hex(id(names)))
print("-----------")
print(type(names))
print(id(names))
print(hex(id(names)))

print("-----------")
#Addition of Data
names.append("Harry")
names.insert(4,"George")

print(names)
print("-----------")

del names[1]

print(names)
print("-----------")

print(names[1])

print("-----------")

#names.clear()
#print(names)
print("-----------")

ages = [10,20,30,40,50]
fruits = ["apple","orange","banana"]

fruits.sort()

print(fruits)

#names.extend(fruits)
names.extend(ages)
print(names)
print("-----------")

print(names)

#Iteration
for n in names:
    print(n)

class Employee:
    def __init__(self,id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def __repr__(self):
        # msg = self.id, self.name, self.salary
        # print(msg)
        message = "Employee id: {}, name: {}, salary: {}".format(self.id, self.name, self.salary)
        return message

    def __str__(self):
        #msg = self.id, self.name, self.salary
        #print(msg)
        message = "Employee id: {}, name: {}, salary: {}".format(self.id,self.name,self.salary)
        return message

e1 = Employee(1,"John",30000)
e2 = Employee(2,"Fionna",36000)
e3 = Employee(3,"George",50000)


# Sorting User Defined Objects
# Give them a Salary Hike
employees = [e1,e2,e3]
print(e1)
print(employees)

a = 10,20,30
print(a)

for e in employees:
    print(e.id)

stack = [10,20,30]

stack.append(50)
stack.pop()

print(stack)

vctor = [1,2,3,4,5]

from collections import deque
dq = deque()
dq.append(10)
dq.append(30)
dq.append(40)
dq.append(50)
dq.append(60)

print(dq)
dq.popleft()
print(dq)
dq.pop()
print(dq)

# Sorting User Defined Objects
# Give them a Salary Hike
empDict = {101:e1,102:e2,103:e3}
print(empDict.keys())
print(empDict.values())


