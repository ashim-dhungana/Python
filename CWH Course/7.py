#LOOPS

i=1
while(i<4):
    print(i)
    i += 1

print("\n")  
for i in range(1,4):
    print(i)

print("\n")
l1 = ["King",1,2]
for i in l1:
    print(i)

#Exit the loop
print("\n")
for i in range(5):
    if (i==3):
        break
    print(i, end=" ")

#Skip the iteration
print("\n")
for i in range(5):
    if (i==3):
        continue 
    print(i, end="\t")