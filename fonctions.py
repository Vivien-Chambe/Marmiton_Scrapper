def get_first_recipe_link(soup):
    a = soup.find('a', attrs={'class': 'txtgrey'})
    if a is None:
        return None
    return a['href']


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