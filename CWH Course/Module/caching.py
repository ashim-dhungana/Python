from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done for 20")
print(fx(5))
print("Done for 5")

# Second term will be printed fast as the data is stored in cache
print(fx(20))
print("Done for 20")
print(fx(5))
print("Done for 5")