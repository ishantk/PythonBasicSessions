import numpy as np
import time

#A = np.array([10,20,30,40,50])
A = np.array((10,20,30,40,50))
B = [10,20,30,40,50]

print(A)
print(B)

print(A[0])
print(B[0])

print(type(A))
print(type(B))

# NumPy Arrays are OPTIMIZED Lists
# 1. Memory
# 2. Time

print("*****Memory******")
P = list(range(100))
print(P)

Q = np.arange(100)
print(Q)

print("Size of list P", P.__sizeof__()) # More on Memory
print("Size of list Q", Q.__sizeof__()) # Less on Memory

print("*****Time******")

startTime = time.time()
print(startTime)

for elm in P:
    print(elm)

endTime = time.time()
print(endTime)

timeDiff = endTime - startTime
print("Time Taken is:",timeDiff)

"""
P i.e. list
Time Taken is: 0.1256241798400879

Q i.e. NumPy Array
Time Taken is: 0.07274699211120605
"""