        #1. What is miltithreading
    #A thread is a lightweight unit of executon within a program

-->Without Multithreading

        Task 1
         ↓
        Task 2
         ↓
        Task 3


-->With Multithreading


        Task 1 ─┐
        Task 2 ─┼── Run simultaneously
        Task 3 ─┘
        


-->When to use Threads

✅ Network requests

✅ File downloads

✅ Log processing

✅ API calls

❌ CPU-intensive mathematical computations (consider multiprocessing instead)
