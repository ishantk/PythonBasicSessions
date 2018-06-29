def dataGenerator():
    file = "datafile.csv"
    for row in open(file,"r"):
        # print(row)
        yield row

dg = dataGenerator()
print(type(dg))

print(next(dg))
print(next(dg))
print("===============")
for data in dg:
    print(data)