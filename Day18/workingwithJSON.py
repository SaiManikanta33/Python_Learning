        #Working with JSON
    #JSON is one of the most common data formmats for API's configuration files,and security tools
    
#Write JSON

import json
employee = {
    "name":"Sai",
    "role":"SOC Analyst",
    "experience":1
}
with open("Day18/employee.json","w")as file:
    json.dump(employee,file,indent=4)
    
    
#Reading JSON
import json
with open("Day18/employee.json","r")as file:
    data = json.load(file)
print(data["name"])
print(data["role"])