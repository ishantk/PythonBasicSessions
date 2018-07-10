import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets.samples_generator import make_blobs

# Software Engrs
X1 = [1, 2, 3, 4, 5] # Years of Experience
Y1 = [20000, 27000, 33000, 35000, 40000] # Salary


# Accountants
X2 = [1, 2, 3, 4, 5]
Y2 = [18000, 19000, 20000, 23000, 25000]

plt.scatter(X1, Y1, c='r', s=30, label='SE')
plt.scatter(X2, Y2, c='g', s=30, label='ACC')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc=2)
plt.show()

print("==========SVM Demo===========")

X, Y = make_blobs(n_samples=40, centers=2, random_state=20)

clf = svm.SVC(kernel="linear", C=1)

clf.fit(X, Y)

plt.scatter(X[:, 0], X[:, 1], c=Y, s=30, cmap=plt.cm.Paired)

plt.show()