from bs4 import BeautifulSoup
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def OpenTextBox():
    import tkinter as tk
    from tkinter import simpledialog
    root = tk.Tk()
    root.withdraw()
    user_input = simpledialog.askstring(title="Recette?", prompt="Entrez le nom d'une recette : ")
    return user_input

recette = OpenTextBox()
driver = webdriver.Chrome("chromedriver")

#TODO entrer un nom de recette et scrapper la première sur la page

driver.get(f"https://www.cuisineaz.com/recettes/recherche_terme.aspx?recherche={recette}")

soup = BeautifulSoup(driver.page_source, 'html.parser')

def get_first_recipe_link(soup):
    a = soup.find('a', attrs={'class': 'txtgrey'})
    if a is None:
        return None
    return a['href']

recipe_link = get_first_recipe_link(soup)

if recipe_link is not None:
    driver.get("https://www.cuisineaz.com{}".format(recipe_link))
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

else:
    print("Pas de recette trouvée")
    exit(1)




def get_recipe_name(soup):
    a = soup.title.text
    if a.startswith("Recette "):
        a = soup.title.text[8:-1] # [8:-1] pour enlever "Recette"
    if a.endswith(" - Recette de cuisine"):
        a = soup.title.text[:-20]
    if a.endswith("| CuisineAZ"):
        a = soup.title.text[:-11]
    print(a)
    return a

#TODO recuperer temps de préparation et temps de cuisson
def get_preparation_time(soup):
    a = soup.find("li", attrs={"id":"trPrepa"})
    trprepa = a.find("span").text
    return trprepa

def get_cooking_time(soup):
    a = soup.find("li", attrs={"id":"trCuisson"})
    trcuisson = a.find("span").text
    return trcuisson

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

def get_recipe(soup):
    title = get_recipe_name(soup)
    preparation_time = get_preparation_time(soup)
    cooking_time = get_cooking_time(soup)
    nb_people = get_number_of_people(soup)
    ingredients = get_ingredients(soup)
    return title, preparation_time, cooking_time, nb_people, ingredients


def print_recipe(title, preparation_time, cooking_time, nb_people, ingredients):
    print(f"Recette : {title} pour {nb_people}")
    print(f"Temps de préparation : {preparation_time} - Temps de cuisson : {cooking_time}")
    print("Ingrédients :")
    for ingredient in ingredients:
        print(ingredient)

print_recipe(*get_recipe(soup))

driver.close()
exit()