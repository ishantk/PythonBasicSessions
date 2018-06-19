file = open("Session3.py","r")
# print(type(file))

# Reading the entire file
# data = file.read()
# print(data)
#
# print(type(data))

# Reading the line
#data = file.readline()
#print(data)

# Limit the read operation
#data = file.read(100)
#print(data)

# Once the data is read, re reading the same data isnt allowed
data = file.read()
print(data)

print("----------------")

data1 = file.read()

print(data1)

# Close the File and Release the memory
file.close()

print(file.closed)

print("----------------")

# Cant read the data if file is closed. Error at Runtime
# data2 = file.read()
# print(data2)

