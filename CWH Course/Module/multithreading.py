import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
   
def main(): 
    # func(2)
    # func(3)

    t1 = threading.Thread(target=func, args=[2])
    t2 = threading.Thread(target=func, args=[3])

    t1.start()
    t2.start()
    
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future = executor.submit(func,3)
        print(future.result())
        future = executor.submit(func,2)
        print(future.result())
        
poolingDemo()