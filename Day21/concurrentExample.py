        #4. Using concurrent.futures
    #This is the recommended way to manage thread pools.

from concurrent.futures import ThreadPoolExecutor
import time
def square(number):
    time.sleep(1)
    return number * number

numbers = [1,2,3,4,5]
with ThreadPoolExecutor(max_workers=3)as executor:
    results = executor.map(square,numbers)
    
for result in results:
    print(result)
    
    
        #5. Thread-safe Counter with Locks
    #When multiple threads modify shared data,use a lock.

import threading
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1
threads = []
for _ in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
    
print(counter)