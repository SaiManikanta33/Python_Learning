

    #3. Creating your First Process
    
from multiprocessing import Process
def greet():
    print("Hello from process!")
        
if __name__ == "__main__":
    process = Process(target=greet)
    
    process.start()
    process.join()
    
    print("Main process Finished")
    
    #On windows the if __name__ == "__main__": guard is required when using multiprocessing.


    #4. Passing Arguments to a process
    
from multiprocessing import Process

def square(number):
    print(number * number)
    
if __name__ == "__main__":
    process =Process(target=square,args=(5,))
    
    process.start()
    process.join()
    
    
    #5. using a process pool
    
from multiprocessing import Pool
def cube(number):
    return number ** 3

if __name__ == "__main__":
    with Pool(processes=4)as pool:
        result = pool.map(cube,[1,2,3,4,5])
    
    print(result)
    
    
    #6. Sharing data between Processes
    #  Use a Queue:
    
from multiprocessing import Process , Queue
def worker(queue):
    queue.put("Task Completed")
    
if __name__ == "__main__":
    queue = Queue()
    process = Process(target=worker,args=(queue,))
    process.start()
    process(ueue.get())
    process.join()