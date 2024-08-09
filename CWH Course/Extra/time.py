import time

t1 = time.time()
for i in range(1000):
    print(i)
t2 = time.time()

print(f"\nTime taken = {t2-t1}")

print(7)
time.sleep(2)
print("This is printed after 2 seconds")


t = time.localtime()
print(t)    #Gives a tuple of the local date and time

formatted_time = time.strftime("%Y-%m-%d  %H:%M:%S", t)
print(formatted_time)