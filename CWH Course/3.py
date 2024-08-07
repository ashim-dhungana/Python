#STRINGS

#Strings are immutable: Original cannot be changed

name = "Ashim"
length = len(name)

print(length)
print(name[1:4])
print(name[-4:-1])
print(name[1:]) #same as name[1:len(name)]
print(name[:4]) #same as name[0:4]
print(name[0:5:2])

print(name.upper())
print(name.lower())

newname = input("Enter your name: ")
print(f"You are amazing {newname}")

letter = '''\nDear <Name>,
You are fucking Great!
<Date>'''

print(letter.replace("<Name>","Ashim").replace("<Date>","1 January, 2040"))