import os
import glob

files = glob.glob("*.py")
print(files)
print(type(files))
for f in files:
    print(f)


path = "/Users/ishantkumar/Downloads/Test.java"

flag = os.path.exists(path)
print(flag)
print("Is Existing",flag)

flag = os.path.isdir(path)
print("Is Directory",flag)

flag = os.path.isfile(path)
print("Is File",flag)

# file = os.listdir(path)
# print(file)
# print(type(file))
#
# for f in file:
#     print(f)

"""
NOTES:
Python File Handling

	Introduction to MySQL (DataBase)

	Unstructured/Structured

	Persistence
		Files
		DB

	Database is to store data permanently
		- SQL
			RDBMS -> MySQL/Oracle
			Tables : Rows and Columns
		- NoSQL
			MongoDB
			Firebase
			Firestore

		SQL : Structured Query Language	

	class Employee:
		def __init__(self, id, name, salary):
			self.id = id	
			self.name = name
			self.salary = salary

	e1 = Employe(1,"John",30000)

	e1.name = "John Watson"
	e1.salary = 50000

	del e1
	
		create table Employee(
			id integer,
			name varchar(256),
			salary integer
		)	

	insert into Employee values(1,"John",30000)
	insert into Employee values(2,"Jennie",40000)		

	update Employee set name = "John Watson", salary = 50000 where id = 1

	delete from Employee where id = 1

	select * from Employee

"""