            #What is module 
        #A module is a python file(.py) containing functions , variables or classes that can be reused.
    #caculator.py is created in another file in day6 folder


# now importing caculator.py in this file

import calculator
print(calculator.add(10,5))


        #Or another way to import
    #import the entire module

import math
print(math.sqrt(25))


        #import specific functions
from math import sqrt
print(sqrt(49))


        #import with an alias
import math as m
print(m.pi)
print(m.factorial(5))



            #Built in modules
    #math
import math
print(math.pi)
print(math.sqrt(81))
print(math.ceil(5.2))
print(math.floor(5.9))



            #random
import random
print(random.randint(1,100))
print(random.choice(["Python","Linux","Networking"]))



            #date and time
from datetime import datetime
now=datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)



            #OS
import os
print(os.getcwd())
print(os.listdir())



            #Creating own modulws
    #File: greeting.py created in day6 folder
    
import greeting
print(greeting.hello("Sai"))
