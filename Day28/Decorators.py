    
    
    #1. Functions Are Objects.

# In python functions can be assigned to variables and passed to other functions.

def greet():
    return "Hello!"
message = greet
print(message())

    #2. What is Decoratrs?
# A decorator adds extra functionality to an existing function without changing its original code.

def decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After function")
    return wrapper
@decorator
def say_hello():
    print("Hello World!")
say_hello()