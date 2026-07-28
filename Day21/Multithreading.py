
        #Creating your first thread

import threading
def greet():
    print("Hello from thread!")
    
thread = threading.Thread(target=greet)     #Creates a new thread
thread.start()                             #begins execution
thread.join()                              #waits until the thread finishes
print("Main program finished")



        #Multiple Threads
import threading
import time
def worker(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")
threads = []
for i in range(3):
    t=threading.Thread(target=worker,args=(f"Thread-{i+1}",))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
    
print("All threads completed.")
