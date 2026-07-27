    #4. Email validation
    
import re
email = "User@gmail.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(pattern,email):
    print("Valid Email",email)
else:
    print("Invalid Email",email)
    
    
    #5.  Extract IPv4 Addresses
import re
text="""
client:192.168.1.20
server:10.0.0.5
Gateway:172.16.1.1
"""
ips=re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b",text)
print(ips)

"""  Note:This regex matches IPv4 like patterns 
        but doesn't verify that each octect is within 0-255             """
        
        
        #6.  Extract URLs

import re
text = "Visit https://example.com or http://test.org"
urls=re.findall(r"http?://[^\s]+",text)
print(urls)        