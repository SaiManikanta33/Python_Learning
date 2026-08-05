
import threading
def greet():
    print("Hello from a thread!")
    
thread = threading.Thread(target=greet)
thread.start()                              #start() being the thread.
thread.join()                               #join() waits until the thread finishes.
print("Main program finished.")


    #3. pasing arguments to threads
    
import threading
def greet(name):
    print(f"Hello, {name}")
thread = threading.Thread(target=greet,args=("Sai",))
thread.start()
thread.join()

    #4. Running multiple threads

import threading
import time
def task(name):
    for i in range(3):
        print(name,i)
        time.sleep(2.5)
t1 = threading.Thread(target=task,args=("Thread-1",))
t2 = threading.Thread(target=task,args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()           #Notice how both threads run concurrently. 