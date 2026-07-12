            #File Handling Basics
        #python uses the open() function to work with files
        
        #syntax
"""   file = open("Example.com","mode")"""
    
    #Common modes
    
""" Mode            Description
    r    --->       Read(default)
    w   ---->       write(overwites existing file)
    a   ---->       append
    x   ---->       create a new file
    rb  ---->       read binary files 
    wb  ---->       write binary file   """
    
"""    
            #writing to a file
file=open("notes.txt","w")
file.write("Python is Awesome! \n")
file.write("I am learning file handling.")
file.close()



        #Reading a file
file = open("notes.txt","r")
content=file.read()
print(content)
file.close()


        #Read line by line
file = open("notes.txt","r")
for line in file:
    print(line.strip())
file.close()



            #Appending to a file
file = open("notes.txt","a")
file.write("\n Learning is passion and never stops!")
file.close()



            #Using "with open()"
    #This is the recommended approach because the file closes automatically.
with open("notes.txt","r") as file:
    print(file.read())
    
    #writing
with open("notes.txt","w") as file:
    file.write("Hello, Python!")
    
    
    """
            #Working with CSV Files
        #Python's built-in csv modules makes reading and writing CSV files easy
    #write to a CSV
    
import csv
with open("students.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age","Branch"])
    writer.writerow(["Sai",19,"Cyber Security"])
    
    #The CSV file created in Day7 folder

import csv
with open("students.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)