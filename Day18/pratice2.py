"""import json
college={
    "Name":"Sai",
    "Age":19,
    "Branch":"CSC",
    "Skills":"Blue Team"
}
with open("Day18/college.json","w")as file:
    json.dump(college,file,indent=4)"""
    
    
    
import json
with open("Day18/college.json","r")as file:
    data = json.load(file)
print(data[Name])