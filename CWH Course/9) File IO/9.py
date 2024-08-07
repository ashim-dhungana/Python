#FILE I/O

f = open("file1.txt","r")
data = f.read()
print(data)
f.close()

st = "Ashim is going to be the King."
f = open("file1.txt","w")
f.write(st)
f.close()

st2 = "He is a legend."
f = open("file1.txt","a")
f.write(st2)
f.close()