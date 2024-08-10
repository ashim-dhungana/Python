import threading
import time

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    
# func(2)
# func(3)

t1 = threading.Thread(target=func, args=[2])
t2 = threading.Thread(target=func, args=[3])

t1.start()
t2.start()