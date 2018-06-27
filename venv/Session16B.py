import numpy as np
A = np.linspace(1,5,10)
print(A)


B = np.array([10,20,30,40,50])

print("Minimum",B.min())
print("Maximum",B.max())
print("Sum",B.sum())

X = np.array([[1,2,3],[4,5,6]])
Y = np.array([[1,2,3],[4,5,6]])

Z = X + Y # -,*,/

print(Z)


print("***********")
P = np.array([[1,2,3],[4,5,6]])
Q = np.array([[7,8,9],[10,11,12]])
R = np.vstack( (P,Q) )
print(R)
print("***********")
S = np.hstack( (P,Q) )
print(S)
print("***********")

K = np.array([(1,2,3),(4,5,6)])
print(K)
L = np.sqrt(K)
print(L)
print("***********")
M = np.std(K)
print(M)







