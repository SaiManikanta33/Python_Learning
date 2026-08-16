

    #11. Extrating IP Addresses
        #This is where regex becomes interesting for cybersecurity
        
import re
text = """
Login from 192.168.1.10
Login from 10.0.0.5
Login from 172.16.0.25
"""        
pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
ips = re.findall(pattern,text)
print(ips)
#⚠️ Important: this pattern finds IP-shaped strings, but it doesn't guarantee every match is a valid IPv4 address. Later, you can combine regex with Python's ipaddress module for proper validation


    #12.Extracting email Addresses
import re
text="""
Contact admin@example.com
Support: security@company.org
"""
pattern = r"[\w.-]+@[\w.-]+\.\w+"
emails = re.findall(pattern,text)
print(emails)


    #13.tracting URLs
import re
text = """
Visit https://example.com
or http://python.org
"""
pattern = r"https?://\S+"
urls = re.findall(pattern,text)
print(urls)


    #14.re.sub()
        #sub() replaces mathing text
import re
text = "User password=secret123"
result = re.sub(
    r"password=\S+",
    "password=REDACTED",
    text
)
print(result)
#This is useful when sanitizing logs before sharing them


    #15. Capturing Groups
        #Groups alllow you to exstract specific parts
import re
text = "User: admin IP: 192.168.1.10"
pattern = r"User:\s(\w+)\sIP:\s([\d.]+)"
result = re.search(pattern,text)
print(result.group(1))
print(result.group(2))
print(result.group())


    #16.finditer()
        #finditer() gives you match objects.
import re
text = "IP: 192.168.1.10 and 10.0.0.5"
pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
for match in re.finditer(pattern,text):
    print(match.group())
    print(match.start())
    print(match.end())
#
#
#
#