        #Why Decorators Mater
    #Decorators are commonly used for:
"""     --> Logging
        --> Authentication
        --> Authorization
        --> Performance measurement
        --> Input validation
        --> Retry mechanisms                """
        
    #Example

import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution Time :{end - start:.4f} seconds")
    return wrapper
@timer
def task():
    total = sum(range(1000000))
    print(total)
task()