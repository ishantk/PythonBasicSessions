with open("Session3.py","r") as file:

    print("tell is ",file.tell())

    data = file.read(200)
    print(data)
    print("***************")

    print("tell is ", file.tell())

    data = file.read(200)
    print(data)
    print("***************")

    print("tell is ", file.tell())

    file.seek(500)
    print("tell is ", file.tell())

    print("***************")
    data = file.read(200)
    print(data)

    """
    HW1: Read XMl File
         Convert the data into Employee Object
         Put it in a list
         Sort the list   
         
    HW2: Source Code Analysis
    
    HW3: Generate Source Code on various Algorithms in different PL
         by taking input from User
                 
    """