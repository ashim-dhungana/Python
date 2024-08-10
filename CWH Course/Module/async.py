# Runs all the function parallelly

import time
import asyncio

async def function1():
    time.sleep(2)
    for i in range(2000):
        print (f"Number {i}")
    
async def function2():
    time.sleep(2)
    for i in range(1000):
        print(f"This is number {i}")

async def main():
    # await function1()
    # await function2()
    
    L = await asyncio.gather(
        function1(),
        function2(),
    )
    
asyncio.run(main())