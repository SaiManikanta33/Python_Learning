
            #Function are First-Class Objects
    #In python functions can be assigned to variable, passed as arguments, and returned from other functions
    
def greet(name):
    return f"Hello, {name}"
say=greet
print(say("Sai"))
    
        #Functions as Arguments
def add(a,b):
    return a+b
def calculate(func,x,y):
    return func(x,y)
print(calculate(add,10,20))