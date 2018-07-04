import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("advertising.csv")

print(data)

X = data["TV"].values
Y = data["Sales"].values

print("============")
print(X)
print("============")
print(Y)
print("============")

data = stats.linregress(X,Y)
b1 = data[0]
b0 = data[1]

print("b1 is",b1) # b1
print("b0 is",b0) # b0

# Y = b0 + b1X
# Predict the data for the same input
Y1 = []

for x in X:
    y = b0 + (b1*x)
    Y1.append(y)

print("============")
print(Y1)
print("============")

plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
# plt.plot(X, Y, "ro")
plt.plot(X, Y, "o", X, Y1)
plt.show()

print("*******SCI-KIT***********")
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

regression = LinearRegression()

l = len(X)
X = X.reshape(l,1)

reg = regression.fit(X,Y) # We are providing Training Data

Y1 = reg.predict(X)
print("******************")
print(Y1)
print("******************")
mse = reg.score(X,Y)
print("******************")
print(mse)
print("******************")