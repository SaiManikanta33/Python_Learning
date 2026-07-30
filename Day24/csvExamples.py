    
    #2. Reading CSV Files

import csv
with open("Day24/students.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
        
    #3. Writing to Files
    
import csv
rows = [
    ["Name","Marks"],
    ["sai",95],
    ["Manikanta",80]
]
with open("Day24/Marks.csv","w",newline="")as file:
    writer = csv.writer(file)
    writer.writerows(rows)