            #Decorators
    #A decorator adds functionality to another function without modifying its code

#Basic decorator

    #Simply the decorators is like a nested function.

def decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After function")
    return wrapper
@decorator
def greet():
    print("Hello!")
greet()

#Decorator with arguments

def logger(func):
    def wrapper(name):
        print("Function Started")
        func(name)
        print("Function finished")
    return wrapper
@logger
def welcome(name):
    print(f"Welcome , {name}")
welcome("Sai")



"""                 Wrapper() is copalsory              """