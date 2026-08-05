

    #5. Thread synchronization
#Sometimes multiple threads access the same data.
#use a Lock:

import threading
counter = 0
lock = threading.Lock()
def increment():
    global counter
    with lock:
        counter += 1
threads = []
for _ in range(100):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print(counter)
                #Without the lock, the final value may be incorrect.

                
    #6. ThreadPoolExecutor
#Python also provides a simpler API.

from concurrent.futures import ThreadPoolExecutor
import time
def square(number):
    time.sleep(1)
    return number * number
with ThreadPoolExecutor(max_workers=3)as executor:
    results = executor.map(square,[1,2,3,4,5])
print(list(results))