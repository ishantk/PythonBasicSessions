from matplotlib import pyplot as plt

#Draw a Bar Graph

p = [0.25,1.25,2,2.25,3.25,4.50]
q = [50,40,30,70,80,60]

plt.bar(p, q, label="Python", width=0.5)

a = [0.75,1.75,2.75,3.75,4.75,5.75]
b = [80,90,30,40,60,10]

plt.bar(a, b, label="Dart", width=0.5)

plt.legend()

plt.xlabel("Demand")
plt.ylabel("Jobs")

plt.title("Data")

plt.show()