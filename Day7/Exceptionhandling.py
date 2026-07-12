            #Exception handling 
    #Exception prevent your program from crashing unexpectedly.
#Basic Example

try:
    number = int(input("Enter a number:"))
    print(100/number)
except ZeroDivisionError:
    print("Cannot divide by Zero.")
    
except ValueError:
    print("Please enter a valid integer.")
    
    
    #If i give 0 as input then the output is comes exception because 0 cannot be divide by any number




            #Finally
    #runs whether an exception occurs or not
try:
    file = open("notes.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File noe found.")
finally:
    print("Program finished.")