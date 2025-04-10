import requests

#define a function to find recipes based on ingredients
def find_recipes(ingredients):
    API_KEY = "36a01f740a3f4fafa5a2d22a3ab7cfa6"
    url = f"https://api.spoonacular.com/recipes/findByIngredients"
    
    #set parameters
    params = {
        'ingredients': ingredients,
        'number': 1,  #number of recipes to return
        'apiKey': API_KEY
    }

    #get request function based on url and parameters
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()  #return data in json format
    else:
        return None  #return none if not successful

#ask user for ingredients they have
ingredients = input("Enter ingredients you have separated by commas: ")

#allow for ingredients with multiple words
ingredients = ','.join([ingredient.strip() for ingredient in ingredients.split(',')])

#find recipes based on ingredients entered
recipes = find_recipes(ingredients)

#check if recipes were found and print them
if recipes:
    for recipe in recipes:
        print(f"Recipe: {recipe['title']}")
else:
    print("No recipes found.")

#define a function to display recipes in a formatted way
def display_recipes(recipes):
    for recipe in recipes:
        #print recipe link
        print(f"Recipe Link: https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-').lower()}-{recipe['id']}")
        #print ingredients the user is missing
        print(f"Ingredients you still need: {', '.join([ingredient['name'] for ingredient in recipe['missedIngredients']])}")
        print("\n")

#print recipe and details
display_recipes(recipes)
