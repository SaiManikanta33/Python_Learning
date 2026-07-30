        #4. Introduction to Pandas
"""

Installation:
    pip install pandas

"""
#Reading a CSV

import pandas as pd
data = pd.read_csv("Day24/students.csv")
print(data)
print(data["Name"])
cyber_students = data[data["Department"]=="Cyber Security"]
print(cyber_students)
sorted_data = data.sort_values(by="Age")
print(sorted_data)


#Basic Statistics
import pandas as pd
data = pd.read_csv("Day24/marks.csv")
print(data["Marks"].mean())
print(data["Marks"].max())
print(data["Marks"].min())