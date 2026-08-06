
#Exercise 1

#Create two processes that print different messages.

"""
from multiprocessing import Process
def msg():
    print("Hello,")
    
def msg2():
    print("Welcome To Python")
    
if __name__ == "__main__" :
    process = Process(target=msg)
    process2 = Process(target=msg2)
    
    process.start()
    process2.start()

    process.join()
    
    
    
    process2.join()
    print("Main Process Finished")
"""

#Exercise 2

#Pass a number to a process and calculate its factorial.

from multiprocessing import Process
import math
def fact(num):
    print(math.factorial(num))

if __name__ == "__main__":
    p=Process(target=fact,args=(5,))
    p.start()
    p.join()
    
    
#Exercise 3

#Use a Pool to calculate squares of numbers from 1 to 10.

from multiprocessing import Pool
def square(num):
    return num * num

if __name__ == "__main__":
    with Pool(processes=5)as pool:
        result = pool.map(square,[1,2,3,4,5])
        
    print(result)
    
    

#Exercise 4

#Use a Queue to send a message from one process to another.

from multiprocessing import Process,Queue
def sender(queue):
    queue.put("hello")
    
def receiver(queue):
    message = queue.get()
    print("Received:",message)
    
if __name__ == "__main__":
    queue = Queue()
    send=Process(target=sender,args=(queue,))
    recieve=Process(target=receiver,args=(queue,))

    send.start()
    recieve.start()

    send.join()
    recieve.join()
    
    
#Exercise 5

#Measure the execution time of a CPU-intensive task using:

#Normal execution
#Multiprocessing

#Compare the results.

from multiprocessing import Pool, cpu_count
from time import perf_counter

N = 10_000_000  # Increase this if your computer finishes very quickly.

def sum_of_squares(start, end):
    return sum(i * i for i in range(start, end))

if __name__ == "__main__":
    workers = cpu_count()
    chunk_size = N // workers

    ranges = []
    for i in range(workers):
        start = i * chunk_size
        end = N if i == workers - 1 else (i + 1) * chunk_size
        ranges.append((start, end))

    # Normal execution
    start_time = perf_counter()

    normal_result = sum(sum_of_squares(start, end) for start, end in ranges)

    normal_time = perf_counter() - start_time
    print("Normal result:", normal_result)
    print("Normal execution time:", round(normal_time, 4), "seconds")

    # Multiprocessing execution
    start_time = perf_counter()

    with Pool(processes=workers) as pool:
        results = pool.starmap(sum_of_squares, ranges)

    multiprocessing_result = sum(results)
    multiprocessing_time = perf_counter() - start_time

    print("\nMultiprocessing result:", multiprocessing_result)
    print("Multiprocessing execution time:", round(multiprocessing_time, 4), "seconds")