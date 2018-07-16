from matplotlib import pyplot as plt
import numpy as np

def sigmoid(inputs):
    outputs = []

    for x in inputs:
        cal = 1 / (1+np.exp(-x))
        outputs.append(cal)

    return outputs

def softMax(inputs):
    outputs = np.exp(inputs) / sum(np.exp(inputs))
    return outputs

inputs = list(range(0,21))
print(inputs)

# outputs = sigmoid(inputs)
outputs = softMax(inputs)

print(outputs)

plt.plot(inputs,outputs)
plt.xlabel("Inputs")
plt.ylabel("Sigmoid")
plt.show()