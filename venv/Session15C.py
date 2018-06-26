from matplotlib import pyplot as plt

# Draw a Scatter Graph

x1 = [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5]
y1 = [8,8.5,9,9.5,10,10.5,11,11.5,12,12.5]

x2 = [9,9.5,10,10.5,11,11.5,12,12.5,13,13.5]
y2 = [3,3.5,4,4.5,5,5.5,6,6.5,7,7.5]

plt.scatter(x1,y1,label="Nike Shoes",color='r')
plt.scatter(x2,y2,label="Nike T-Shirts",color='g')

plt.title("Nike")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.legend()

# so that plot can be visible
plt.show()

