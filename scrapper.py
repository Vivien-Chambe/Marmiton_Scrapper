from bs4 import BeautifulSoup
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:\\Users\\vivie\\Downloads\\chromedriver_win32\\chromedriver")

ingredients = []
driver.get("https://www.cuisineaz.com/recettes/gratin-dauphinois-simplissime-7094.aspx")
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

a = soup.find_all('ul', attrs={'txt-dark-gray'})
b = soup.find_all('li') 

for i in soup.find_all('section', attrs={'borderSection ingredients'}):
    for element in i.findAll(attrs={'class': 'txt-dark-gray'}):
        for span in element.findAll('span'):
            print(span.text)


driver.close()
exit()