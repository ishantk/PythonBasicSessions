a = 10
b = 2.2
c = 'x'
name1 = 'John Watson'
name2 = 'John Watson'
#shopName = 'John\'s Cakes'
shopName = "John's Cakes & Coffee"
#message = "This is a great day to start with" \
#          "we shall learn Python !!"

message = """This is Awesome
John's got admission in College !!             
Lets Learn Python"""

print(type(a))
print(type(b))
print(type(c))
print(type(name1))
print(shopName)
print(message)

print(hex(id(name1)))
print(hex(id(name2)))

# STRINGS ARE IMMUTABLE
# Strings cannot be changed.
# name3 = name1.upper()

name1 = name1.upper()
print("name1 is",name1)
#print("name3 is",name3)

print(name1[0])
print(name1[-1])

print(len(name1))

for i in range(-1,-(len(name1)+1),-1):
    #print(name1[i])
    print(name1[i], end='')

print()
names = "  John, Jennie, Jim, Jack, Joe  "
newNames = names.strip()
print(names.strip())
print(names)

nm = names.split(",")
print(type(nm))


a = [10,20]
print(a)
print(a[0])
print(a[1])

print(nm[0].strip())
print(nm[1].strip())


#Slicing a String
names = "John, Jennie, Jim, Jack, Joe"

print(names[0:3])
print(names[3:6])

print(names[3:])

print(names[:5])

print("data is ",names[-4:])

#MUATBLE SEQUENCE
myList = ['John','Jennie',10,2.2,'Awesome']
yourList = [10,20,30,40,50]

print("-----------")

for x in yourList:
    print(x)

myList.append(100)
myList.append('Wow')

print(myList)

ourList = list(range(1,101))
print(ourList)

#Methods on String and List

songName = "song_1_english.mp3"
print (songName.endswith(".mp3"))
print (songName.startswith("song_"))
print (songName.find("english"))

newSongName = songName.replace('s','t')

print (songName.replace('s','t'))
print (songName)
print (newSongName)

party1Punjab = 123

party1 = [123,4567,23457,8752,1234]
party2 = [456,4567,23344,3432,145]

votes = [[123,4567,23457,8752,1234],[456,4567,23344,3432,145]]
votes = [[[123,4567,23457,8752,1234],[456,4567,23344,3432,145]],[[123,4567,23457,8752,1234],[456,4567,23344,3432,145]]]

print (len(party1))
print (len(party2))
print (len(votes))
print (len(votes[0]))
print (len(votes[1]))


names = ['John','Jennie']
names.append('Jack')
names.insert(1,'Mike')

names.clear()

moreNames = ['George', 'Leo']

names.extend(moreNames)

print ("names: ",names)

l1 = ['a','b']
l2 = ['a','b']


print (hex(id(l1)))
print (hex(id(l2)))

myList = [10,20,30]
myTup = (10,20,30)

myList[0] = 100
myTup[0] = 100

print (myList)
print (myTup)



