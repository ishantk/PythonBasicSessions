print("==App Started==")

a = 10
b = 2
c = 0



list = [10,20,30,40,50]



try:
    c = a / b
    print("list[20] is",list[20])
    #print("This is Awesome")
# except IndexError as iRef:
#     print(iRef)
except Exception as e:
    print(e)
finally:
    print("This is Awesome")


print("c is",c)
print("==App Finished==")