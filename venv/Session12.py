from tkinter import *

def onClick():
    name = entryName.get()
    age = entryAge.get()
    email = entryEmail.get()
    address = entryAddress.get()

    print("You Entered {}, {}, {}, {}".format(name,age,email,address))


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
