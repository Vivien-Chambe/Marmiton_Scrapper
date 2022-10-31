from bs4 import BeautifulSoup
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from fonctions import *
from myownmodule import OpenTextBox

recette = OpenTextBox()
driver = webdriver.Chrome("chromedriver")

#TODO entrer un nom de recette et scrapper la première sur la page

driver.get(f"https://www.cuisineaz.com/recettes/recherche_terme.aspx?recherche={recette}")

soup = BeautifulSoup(driver.page_source, 'html.parser')

recipe_link = get_first_recipe_link(soup)

if recipe_link is not None:
    driver.get("https://www.cuisineaz.com{}".format(recipe_link))
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    print_recipe(*get_recipe(soup))

else:
    print("Pas de recette trouvée")
    exit(1)




driver.close()
exit()