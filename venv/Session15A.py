from matplotlib import pyplot as plt
from matplotlib import style

#Drawing a Line Graph with more than 1 line

x1 = [5,7,9]
y1 = [12,10,8]

x2 = [6,9,11]
y2 = [6,1,7]

plt.plot(x1,y1,'g',label="cse",linewidth=3)
plt.plot(x2,y2,'c',label="me",linewidth=5)

#Add titles
plt.title("Branches")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.legend()

plt.grid(True,color='g')

plt.show()