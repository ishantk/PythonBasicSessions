def show():
    return "A"

s = show

print(s())
print(s())
print(s())

print("=============")

# Generator
def showAgain():
    yield "B"
    yield "C"
    yield "D"
    yield "E"
    yield "F"

sa = showAgain()
# print(sa)
#
print(type(s))
print(type(sa))

# Generator in Action:
print(next(sa))
print(next(sa))
print(next(sa))
print(next(sa))
print(next(sa))
print(next(sa))