import pandas as pd

s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series(["John","Jennie","Jim","Jack","Joe"])

print(type(s1))
print(s1)
print("----")
print(s2)

df = pd.DataFrame([s1,s2])
print(df)

"""df = pd.DataFrame(
    [
        [101,201],
        ["John","Jennie"]
    ]
)"""

df = pd.DataFrame(
    [
        [101,201],
        ["John","Jennie"]
    ],
    index=["Roll Number","Name"],
    columns=["C1","C2"]
)

print("----")
print(df)
print("----")
print(df.loc["Roll Number":"Name","C1"])

df = pd.DataFrame(
    {
        "roll":[101,102,103,104,105],
        "name":["John","Sia","Mike","Leo","Fionna"]
    }
)
print("*******")
print(df)

print("*******")
#Maths on DataFrame
print(df["roll"]/2)

df1 = df["roll"] > 102
print(df1)

# Try in Jupyter Notebook
# df["roll"].plot(kind="hist")