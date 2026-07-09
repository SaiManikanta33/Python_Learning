            #Dictionarires
            #a dictionary stores data as key-value pairs
student={
    "name":"Sai",
    "age":19,
    "branch":"Cyber Security"
}
print(student["name"])
print(f"student:{"age"}")


        #Add or Update Values
student["College"]= "Raghu Engineering College"     #Add
student["age"] = 20         #update
print(student)


            #iterate through a Directory
for key,value in student.items():
    print(key,":",value)