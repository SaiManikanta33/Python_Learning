            # 1. Regex is Regular Expressions
    #A regular expression(Regex) is a sequence of characters thet define a search pattern
    #Import module


import re

#example

import re
text="Python is qwesome"
match=re.search("Python",text)
if match:
    print("Found!")
    
    #2. Common regex functions
#  re.search()
    #finds the first match
    
import re
text="My Ip is 192.168.1.10"

result = re.search (r"\d+\.\d+\.\d+\.\d+",text)
print(result.group())


#re.findall()
import re
text = "Ports:22,80,443"
ports = re.findall(r"\d+",text)
print(ports)


#re.sub()
    #replacing matching text
import re
text = "User password is secret123"
new_text = re.sub("secret123","**********",text)
print(new_text)
