

    #3. Understanding *args
# *args allows a function to accept any number of positional arguments.

def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(add(2,4))
print(add(1,2,3,4,5))


    #4. **kwargs
# **kwargs allows a function to accept any number of keyword arguments
def display(**student):
    for key,value in student.items():
        print(key,":",value)
display(
    name="Sai",
    branch="Cyber Security",
    year=2,
)


    #5. Decorators with arguments
def logger(func):
    def wrapper(*args,**kwargs):
        print(f"Calling{func.__name__}")
        result = func(*args,**kwargs)
        print("Finished")
        return result
    return wrapper
@logger
def multiply(a,b):
    return a*b
print(multiply(4,6))
def multi(x,y):
    return x*y
print(multiply(10,20))


    #6. Timing Function Execution

import time
def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"Execute Time: {end - start:.4f} seconds")
        return result
    return wrapper
@timer
def calculate():
    total =0
    for i in range(10000000):
        total += i
    return total
calculate()