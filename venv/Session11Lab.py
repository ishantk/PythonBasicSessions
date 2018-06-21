import mysql.connector
from tkinter import *

def saveInDB(name, age, email, address):
    sql = "insert into Student values(null,'{}',{},'{}','{}')".format(name, age, email, address)
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="GW2018AI")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    print(name, " Saved in DB")

#saveInDB("Sia",30,"sia@example.com","Redwood Shores")


def onClick():
    name = entryName.get()
    age = entryAge.get()
    email = entryEmail.get()
    address = entryAddress.get()

    print("You Entered {}, {}, {}, {}".format(name,age,email,address))
    saveInDB(name,age,email,address)

# is a window i.e. a Frame which is visible as a UI
root = Tk()

# Textual information
lblTitle = Label(root,text="Welcome to Auribises")
lblTitle.pack()
#lblTitle.grid(row=0,column=0)

lblName = Label(root,text="Enter Your Name")
lblName.pack()

entryName = Entry(root)
entryName.pack()

lblAge = Label(root,text="Enter Your Age")
lblAge.pack()

entryAge = Entry(root)
entryAge.pack()

lblEmail = Label(root,text="Enter Your Email")
lblEmail.pack()

entryEmail = Entry(root)
entryEmail.pack()

lblAddress = Label(root,text="Enter Your Address")
lblAddress.pack()

entryAddress = Entry(root)
entryAddress.pack()

btnSubmit = Button(root,text="Submit",command=onClick)
btnSubmit.pack()

root.mainloop()


class Student:

    def __init__(self, roll, name, age, email, address):
        self.roll = roll
        self.name = name
        self.age = age
        self.email = email
        self.address = address

    def showStudent(self):
        print("Roll Number {} belongs to {}".format(self.roll,self.name))

    def getStudentDetails(self):
        data = "{},{},{},{},{}\n".format(self.roll, self.name, self.age, self.email, self.address)
        return data

s1 = Student(1,"John",20,"john@example.com","Redwood Shores")
s2 = Student(2,"Jennie",30,"jennie@example.com","Country Homes")

s1.showStudent()
s2.showStudent()

# Since we wish to persist data
# Write the data in Database

# Since we wish to persist data
# Write the data in file
"""
file = open("students.txt",'a') #a -> append mode
data = s2.getStudentDetails()
file.write(data)
file.close()

print("Data Saved")
"""

#con = mysql.connector.connect(user="root",password="",host="127.0.0.1",database="GW2018AI")
#print("Is Connection Established:",con.is_connected())
#print(type(con))
# cursor = con.cursor()
#print(type(cursor))

# sql1 = "insert into Student values(null,'Fionna',30,'fionna@example.com','Redwood Shores')"
# sql2 = "insert into Student values(null,'{}',{},'{}','{}')".format(s1.name,s1.age,s1.email,s1.address)
# sql3 = "insert into Student values(null,'{}',{},'{}','{}')".format(s2.name,s2.age,s2.email,s2.address)
#
# cursor.execute(sql2)
# cursor.execute(sql3)
# con.commit()
# print("Student Saved !!")

#sql = "select * from Student"
#cursor.execute(sql)

# row = cursor.fetchone()
# print(row)
# row = cursor.fetchone()
# print(row)

"""students = []

for row in cursor:
    print(row)
    s = Student(row[0],row[1],row[2],row[3],row[4])
    students.append(s)

print(students)"""

# Read row by row and convert every row into Student Object
# And create a list of Student objects
# Sort on the basis of name/roll/age