import numpy as np
#A = np.array([(10,20,30),(40,50,60),(30,40,70),)
#B = np.array([(10,20,30)])
#A = np.array([[10,20,30],[40,50,60],[30,40,70]])
#B = np.array([10,20,30])
"""A = np.array([ [ [10,20,30],[30,40,70] ],[ [10,20,30],[30,40,70] ]])
B = np.array((10,20,30))




print(A)
print(B)
print(type(A))

print(A[0])
print(A[0][1])"""

# A = np.array([10,20,30])
# A = np.array([[10,20,30],[20,30,40]])
# A = np.array([ [[10,20,30],[20,30,40]] , [[10,20,30],[20,30,40]] ])

#print("Dimension of A Array",A.ndim)
#print("Dimension of B Array",B.ndim)

A = np.array([10,20,30,40,50,60])
print("Size: ",A.itemsize)
print("Size: ",A.__sizeof__())
print("Size: ",A.size)

print("DataType",A.dtype)
print("Shape ",A.shape)

B = np.array([[10,20,30],[40,50,60]])
print("Shape ",B.shape)

print("***********************")
# SHAPE IS IMMUTABLE
P = np.array([[10,20,30],[40,50,60]])
print(P)
print(P.shape)
Q = P.reshape(3,2)

print("***********************")

print(Q)
print(Q.shape)

print("***********************")

print(P)
print(P.shape)

print(P[0,1]) # Slicing
print(P[0][1])
print("***********************")

print(P[0:,2]) # Slicing
print(P[0:2,1]) # Slicing


