from pandas import DataFrame, read_csv
import matplotlib.pyplot as plot
import pandas as pd
import sys
import matplotlib

"""print("Python Version is: ",sys.version)
print("Pandas Version is: ",pd.__version__)
print("Matplotlib Version is: ",matplotlib.__version__)

#Data
streams = ["cse","ece","me","ce","ee"]
students= [200,120,200,100,120]

#Merge Data

dataSet = list(zip(streams,students))
print(dataSet)

# Use Pandas to create a DataFrame
df = pd.DataFrame(data=dataSet,columns=["Streams","Students"])
print(df)

df.to_csv("studentsData.csv",index=False,header=False)
print("DataFrame written to File")
"""

#df = pd.read_csv("studentsData.csv")
# df = pd.read_csv("studentsData.csv",header=None)
"""df = pd.read_csv("studentsData.csv",names=["Streams","Students"])
print(df)

print(df.dtypes)

# Analysis on DataFrames
# sdf = df.sort_values(["Streams"],ascending=True)
sdf = df.sort_values(["Students"],ascending=True)

print("----------------")

print(sdf)

print("----------------")

#print(sdf.head(1))
print(sdf.head(2))

print("Max Number of Students:",df["Students"].max())

plot.plot(df["Streams"],df["Students"])
plot.title('Data')
plot.ylabel('Students')
plot.xlabel('Streams')
plot.show()
"""

df = pd.read_csv("datafile.csv",header=None,names=["SrNo","Cases Reported"])
print(df)