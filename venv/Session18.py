# def add(a=10, b=20):
#     return a+b

def add(a, b):
    return a+b

fun = add

print(add(10,20))
print(fun(30,40))

print(type(add))
print(type(fun))

print(hex(id(add)))
print(hex(id(fun)))

#Lambdas | Anonymous Function | Single Line Functions
lm1 = lambda x, y : x*y

print(lm1(10,20))
print(type(lm1))

# def square(num):
#     return num*num

def square(num1, num2, num3):
    return num1*num2*num3

lm2 = lambda x, y, z : x*y*z

#Maps
# m1 = map(square,[1,2,3,4,5],[3,4,5,6,7],[9,8,7,6,5])
m1 = map(lm2,[1,2,3,4,5],[3,4,5,6,7],[9,8,7,6,5])
print(m1)
print(type(m1))
print(list(m1))

#Maps with lambdas and dictionary
emps = [{"eid":101,"name":"John"},{"eid":201,"name":"Jennie"}]
lm3 = lambda dic : dic["eid"]
result = map(lm3,emps)
print(list(result))

lm4 = lambda dic : dic["name"] == "John"
result = map(lm4,emps)
print(list(result))

#Multiple Lists
lm5 = lambda P, Q : P + Q
L1 = [10,20,30,40,50]
L2 = [30,40,50,60,70]
result = map(lm5,L1,L2)
print(list(result))

#Filters
L3 = [10,20,30,40,11,12,13,14,15,16]
lm6 = lambda n : n%2 == 0
result = map(lm6,L3)
print(list(result))

#Filter on List
filterResult = filter(lm6,L3)
print(list(filterResult))

#Filter on Dict
filterResult = filter(lm4,emps)
print(list(filterResult))

#List Comprehensions
A = [10,20,30,40,50]
B = [x*x for x in [1,2,3,4,5]]
C = [x*x for x in [1,2,3,4,5] if x%2 ==0]

print(A)
print(B)
print(C)