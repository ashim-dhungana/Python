#LISTS and TUPLES

#Lists are mutable(changeable) but Tuples are immutable

new = ["Apple", "Mango", 7, False, 3.33, "Ashim"]

print(new[4])
new[4] = 6.66
print(new[4])

#Adding values

new.append("King")
print(new)
new.insert(5,"Inserted")
print(new)

#Removing Values

print(new.pop())
print(new)
new.remove("Inserted")
print(new)

new.reverse()
print(new)


#TUPLES

print("\n")

one = (1,"First")
another = (7, 3.44, "New", 7, "Old")
print(another.count(7))
new_tuple = one + another
print(new_tuple)