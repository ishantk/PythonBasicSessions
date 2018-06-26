from matplotlib import pyplot as plt

# Pie Chart
activities = ["coding","outing","playing"]
slices = [7,2,3]
cols = ['r','g','b']
explode = (0.1,0,0)

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=explode
        )

plt.legend()
plt.title("Training")
plt.show()