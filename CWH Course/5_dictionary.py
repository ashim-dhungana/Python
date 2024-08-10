#DICTIONARY and SETS

marks = {
    "Tony":100,
    "Steve":77.5,
    "Tommy":"Fail"
}

print(marks["Steve"])
marks.update({"Steve":70})
print(marks["Steve"])       #Returns Error
print(marks.get("Tony"))    #Returns None

print(marks.keys())
print(marks.values())
print(marks.items())


#Sets

print("\n")
new_marks = {3,4,7,2,"Ashim",5,4,"Ashim",2}
another_marks = {6,7,8,9}
print(new_marks)

new_marks.add(555)
print(new_marks)

new_marks.remove(4)
print(new_marks)

print(new_marks.union(another_marks))
print(new_marks.intersection(another_marks))

print(new_marks.clear())