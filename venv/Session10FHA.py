file = open("/Users/ishantkumar/Downloads/employees.xml","r")
# data = file.read()
# print(data)

data = file.readlines()

print(len(data))

print(type(data))

# for line in data:
#     print(line)

print(data[0])