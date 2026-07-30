        #Installation Required packages
        
    #-->    pip install requests beautifulsoup4
    
#Verify:
"""
import requests
from bs4 import BeautifulSoup
print("Libraries installed successfully")


    #Html Basics

#3. Fetch a webpage   
import requests
url = "https://google.com"
response = requests.get(url)
print(response.status_code)
print(response.text[:300])


#4. Parse html with beutifulsoup
import requests
from bs4 import BeautifulSoup
url = "https://google.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
print(soup.title.text)


#5. Extract Elemets
#Extract all links

import requests
from bs4 import BeautifulSoup
url = "https://google.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
print(soup.title.text)

for link in soup.find_all("a"):
    print(link.get("href"))

#Exstract All headings
for heading in soup.find_all("h1"):
    print(heading.text)
    
#Exstract paragraphs
for para in soup.find_all("p"):
    print(para.text)    """
    
    
# Find Elements by class or ID
#   <p class="news">Latest Update</P

import requests
from bs4 import BeautifulSoup
url = "https://google.com"
response = requests.get(url,timeout=10)
response.raise_for_status()
soup = BeautifulSoup(response.text,"html.parser")
news = soup.find(class_="news")
if news:
    print(news.text)
    
element = soup.find(id="main")
if element:
    print(element.text)