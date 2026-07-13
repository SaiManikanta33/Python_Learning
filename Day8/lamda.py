            #Lamda
    #lamda function is a small anonymous function.
    
        #Syntax
    #lambda variable:expression
    
#normal function

def square(x):
    return x*x
print(square(5))

#lamda function

square=lambda x:x*x
print(square(5))

#Multiple parameters
add=lambda a,b:a+b
print(add(10,20))