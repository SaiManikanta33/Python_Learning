

1. Synchronous vs Asynchronous

-->Synchronous Execution
Tasks run one after another.
    Task 1 --> Task 2 --> Task3 -->Task3
if Task 1 takes 5 seconds, the other must wait

Asynchrounous Execution:
    Task 1
    Task 2
    Task 3
      ↓
    Run concurrently while waiting for I/O

This id ideal for:
--> API Requests
--> Downloading files
--> Reading network data
--> Web scraping
--> Cloud automation


6. When should you Use Async?
Use async for:
    . Web APIs
    . Downloading files
    . Cloud services
    . Database requests
    . Multiple requests

Avoid async for:
    . Heavy mathematical calculations 
    . Image processing
    . Password hashing
    . CPU-intensive work
For CPU-bound work , prefer multiprocessing