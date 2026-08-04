

    #4. Generator Expression
#Generator expression:
squares = (x * x for x in range(5))
for value in squares:
    print(value)

#Comapre

#List Comprehension
[x * x for x in range(5)]
#Generator expression
(x * x for x in range(5))

"""
    #5. Reading large files Efficiently
#Instead of:
with open("security.log")as file:
    lines = file.readlines()
"""   
#Use
with open("Day26/security.log")as file:
    for line in file:
        print(line.strip())
        
#This reads one line at a time, making it much more memory efficient.


    #6. Build your own generator.
def even_numbers(limit):
    for number in range(limit):
        if number % 2 == 0:
            yield number
for value in even_numbers(10):
    print(value)