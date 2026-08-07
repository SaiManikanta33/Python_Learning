

#2. Your first Coroutine
"""
import asyncio
async def greet():
    print("Hello1")
    await asyncio.sleep(5)          #Waits 2 seconds
    print("Welcome to Async Python!")
asyncio.run(greet())

#   New Keywords
#   -->async --> Defines a coroutine
#   -->await --> waits for an asynchronous operation to complete.
    #.3. Running Multiple tasks
import asyncio
async def task(name,seconds):
    print(f"{name} Started")
    await asyncio.sleep(seconds)
    print(f"{name} finished")

async def main():
    await asyncio.gather(
        task("Task A",2),
        task("Task B",1),
        task("Task C",10)
    )  
asyncio.run(main())

    #Tasks runconcurrently instead of one after another.

    
    #4. Creating tasks.

import asyncio
async def download(file):
    print(f"Downloading {file}")
    await asyncio.sleep(2)
    print(f"{file} downloaded")
    
async def main():
    task1=asyncio.create_task(download("report.pdf"))
    task2 = asyncio.create_task(download("logs.zip"))
    
    await task1
    await task2
asyncio.run(main())
"""

    #5. Async HTTP Request
    #   pip install aiohttp
    
import aiohttp
import asyncio
async def fetch(url):
    async with aiohttp.ClientSession()as session:
        async with session.get(url) as response:
            print(url,response.status)
async def main():
    await asyncio.gather(
        fetch("https://google.com"),
        fetch("https://python.org")
    )
asyncio.run(main())
#
#
#