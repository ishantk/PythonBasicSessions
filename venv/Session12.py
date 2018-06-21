from tkinter import *

def onClick():
    name = entryName.get()
    age = entryAge.get()
    email = entryEmail.get()
    address = entryAddress.get()

    print("You Entered {}, {}, {}, {}".format(name,age,email,address))

def show():
    print("This is Awesome")

# is a window i.e. a Frame which is visible as a UI
root = Tk()

# Add Menu in UI
menu = Menu(root)
root.config(menu=menu)

fMenu = Menu(menu)
menu.add_cascade(label="File",menu=fMenu)

fMenu.add_command(label="New", command=show)
fMenu.add_command(label="Open")
fMenu.add_command(label="Save")


fEdit = Menu(menu)
menu.add_cascade(label="Edit",menu=fEdit)

fEdit.add_command(label="Cut")
fEdit.add_command(label="Copy")
fEdit.add_command(label="Paste")


fHelp = Menu(menu)
menu.add_cascade(label="Help",menu=fHelp)

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
