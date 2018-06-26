from matplotlib import pyplot as plt

# Area Plot
trainingDays = [1,2,3,4,5]

coding = [7,8,6,12,15]
outing = [2,3,4,5,6]
playing = [3,4,5,6,7]

# plt.plot([],[],color='r',label="coding",linewidth=5)
# plt.plot([],[],color='m',label="outing",linewidth=5)
# plt.plot([],[],color='g',label="playing",linewidth=5)

plt.stackplot(trainingDays,coding,outing,playing,colors=['r','m','g'])

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.title("Training")

plt.legend()

plt.show()
