from bs4 import BeautifulSoup
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:\\Users\\vivie\\Downloads\\chromedriver_win32\\chromedriver")


driver.get("https://www.cuisineaz.com/recettes/gratin-dauphinois-simplissime-7094.aspx")
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

def get_number_of_people(soup):
    a = soup.find("span", attrs={"id":"LblRecetteNombre"})
    return a.text

def get_ingredients(soup):
    ingredients = []
    a = b = c = 0
    for i in soup.find_all('section', attrs={'borderSection ingredients'}):
        a+=1
        for element in i.findAll(attrs={'class': 'txt-dark-gray'}):
            b+=1
            for span in element.findAll('span'):
                c+=1
                ingredients.append(span.text)
    print(a, b, c)
    return ingredients

get_number_of_people(soup)
gratingredients = get_ingredients(soup)


print(gratingredients)
driver.close()
exit()