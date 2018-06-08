data = ["John",10]

print(type(data[0]))
print(type(data[1]))


def fun(* args):
    print(args)
    print(type(args))


fun("John","Jennie","Jack")

tpl = (10,20,30,40,50)
fun(tpl)

fun(10)
fun("John")

names = ["john","jennie"]
ages = [30,40]

fun(names,ages,tpl)