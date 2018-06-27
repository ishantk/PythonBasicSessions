import numpy as np
import matplotlib.pyplot as plt

print(np.pi)
X = np.arange(0, 3*np.pi, 0.1)
print(X)
Y = np.sin(X)
print(Y)

plt.plot(X,Y)
plt.show()