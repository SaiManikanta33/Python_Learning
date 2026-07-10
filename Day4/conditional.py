            #Conditional statements(if,elif,else)
            #if
age=19
if age>=18:
    print("You are eligible to vote.")
    
    
            #if ... else
num=int(input("Enter a number:"))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
    
            #if ... elif ... else
marks=int(input("ENter your marks:"))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")
    
    
            #nested if
age=int(input("Enter age:"))
citizen=True
if age >= 18 :
    if citizen:
        print("Eligible")
    else:
        print("Not a citizen")
else:
    print("Underage")