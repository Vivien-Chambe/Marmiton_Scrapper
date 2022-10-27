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

ingredients_list = a.find_all('li')


driver.close()
exit()