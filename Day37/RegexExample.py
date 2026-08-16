

    #3.re.search()
        #Searches for the occurence of a pattern
        
import re
text = "User logged in from 192.168.1.25"
result = re.search(r"\d+",text)
print(result.group())


    #4.Find one or more
        #Returns all matches
import re
text = "Users:123,456,789"
num = re.findall(r"\d+",text)
print(num)


    #5.match()
        #match() checks only the beginning of a string

import re
text = "Python is powerful"
res=re.match(r"Python",text)
print(res.group())
#But
text = "I love Python"
res = re.match(r"Python",text)
print(res)          #Output is None Because Python isn't at the beginning


    #6.re.fullmatch
        #Checks whether the entire string matches the pattern.
import re
res = re.fullmatch(r"\d+","12345")
print(res.group())
#This mathes
#But
res = re.fullmatch(r"\d+","123abc")
print(res)          #Output is none


print(re.findall(r"\d+","Python123"))


    #8.Character Classes 
        #You can define your own character set.
    #   [1,2,3]
    #Means
    #Match a,b or c
    
import re
text = "cat bat rat"
print(re.findall(r"[cb]at",text))


    #9.ranges
        #You can specify ranges
    #  [a-z]
    #  [A-Z]
    #  [0-9]

print(re.findall(r"[A-Z]","Hello PyThoN"))


    #10.Quantifiers
print(re.findall(r"\d{3}","123 45 78954 222"))