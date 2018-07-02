import pandas as pd

df = pd.read_csv("bengaluru.csv")
# df = pd.read_csv("bengaluru.csv",header=None)
print(df)
print("=======")
print(df.head()) # 1st Five Records
print(df.head(10)) # 1st 10 Records
print(df.tail()) # Last Five Records
print(df.tail(10)) # Last 10 Records
print("=======")
print(df.shape)
print(type(df.shape))
print("***************")
print(df.iloc[0:5,0:2])
print("***************")
print("***************")
print(df.iloc[100:200,:])
print("***************")
print(">>>>>>>>>>>>>>>")
print(df.loc[100:200,["Temperature","Humidity"]])
print(">>>>>>>>>>>>>>>")
print("<<<<<<<<<<<<<<<")
print(df["Temperature"])
print(">>>>>>>>>>>>>>>")
print("<<<<<<<<<<<<<<<")