import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

path_to_chrome_driver = r"C:\Users\Admin\chromedriver"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificte-errors')
options.add_argument('--ignore-ssl-errors')

browser = webdriver.Chrome(executable_path=path_to_chrome_driver,chrome_options=options)
url_to_scrape="http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=0"
browser.get(url_to_scrape)
r=requests.get(url_to_scrape)
soup=BeautifulSoup(r.text,"lxml")

search_results = []
search_result=[]

for table_row in soup.select("#sites-canvas-main tr"):
	table_cells = table_row.find('div',attrs={'class':'sites-search-results-wrapper'})
	
for row in table_cells.findAll('div',attrs={'class':'sites-search-result'}):
    search_result.append(url_to_scrape[0:31]+row.a['href'])
 
print(search_result)

details = {}
for k in range(1,len(search_result)+1):
	search_results=browser.find_element_by_xpath('//*[@id="col0"]/div/div[2]/div['+str(k)+']/h3/a')
	search_results.click()	
	browser.back()

	


	

    