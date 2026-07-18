            #what is a function
#A function is block of code that performs a specific task.
#it helps repetition and makes program easier to maintain

    #Syntax
    
def greet():
    print("Hello ,Welcome to python")
greet()     #calling the function


            #function parameters
    #parameters allow you to pass data into a function
def greet(name):
    print(f"Hello,{name}")
greet("sai")
greet("Manikanta")
greet("Manikanta")

            #multiple parameters
def add(a,b):
    print(a+b)
add(10,20)


            #Retun values
    #instead of printing , a function can return value
def add(a,b):
    return a+b
result=add(15,25)
print(result)

def square(number):
    return number * number
print(square(5))

    #default parameters
def greet(name="Guest"):
    print(f"Hello, {name}")
greet()
greet("Sai")

        #Variable sccope
    #Local Scope
    #declares value at the inner the function
def demo():
    x=20
    print(x)
demo()

    #Global scope
    #declares value at the outer the function
x=100
def show():
    print(x)
show()


            #Recursion
        #A function calling itself
def countdown(n):
    if n == 0:
        print("Done")
    else:
        print(n)
        countdown(n-1)
countdown(5)
