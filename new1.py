import requests
from bs4 import BeautifulSoup
url = input("Enter a website to extract from:")
r = requests.get(url)
data =r.text

soup = BeautifulSoup(data,"lxml")
for link in soup.findAll('a',{'class':'waves-effect'}): #to find all links: soup.findAll('a')
    print(link.get('href'))
