import requests

#define a function to find recipes based on ingredients
def find_recipes(ingredients):
    API_KEY = "36a01f740a3f4fafa5a2d22a3ab7cfa6"
    url = f"https://api.spoonacular.com/recipes/findByIngredients"
    
    #set parameters
    params = {
        'ingredients': ingredients,
        'number': 10,  #maximum number of recipes to return
        'apiKey': API_KEY
    }

    #get request function based on url and parameters
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()  #return data in json format
    else:
        return None  #return none if not successful

def display_recipe(recipe):
    #print recipe name
    title = recipe.get('title', 'Unknown Recipe')  # Use 'title' key
    print(f"Recipe: {title}")

    #print recipe link
    recipe_id = recipe.get('id', 'unknown')  # Use 'id' key
    print(f"Recipe Link: https://spoonacular.com/recipes/{title.replace(' ', '-').lower()}-{recipe_id}")
    
    #print ingredients the user is missing
    missed_ingredients = recipe.get('missedIngredients', [])
    missing = ', '.join([ingredient.get('name', 'unknown') for ingredient in missed_ingredients])
    print(f"Ingredients you still need: {missing}")
    print("\n")

#initial greeting
print("Welcome to the Recipe Generator!")
print("This program will help you find recipes based on the ingredients you have at home.")

#ask user for ingredients they have
ingredients = input("Enter ingredients you have separated by commas: ")

#allow for ingredients with multiple words (ex. "bell pepper")
ingredients = ','.join([ingredient.strip() for ingredient in ingredients.split(',')])

#find recipes based on ingredients entered
recipes = find_recipes(ingredients)

#check if recipes were found and print them
if recipes:
        print("\n")
        print("Here is a recipe you can make:")
        #return one recipe to start
        index = 0
        while index < len(recipes):
            # Display the current recipe
            display_recipe(recipes[index])

            #ask the user if they want to see the next recipe
            while True:
                user_input = input("Would you like to see another recipe? (y/n): ").strip().lower()
                if user_input == 'y':
                    index += 1  #move to the next recipe
                    break
                elif user_input == 'n':
                    print("Enjoy your meal!")
                    exit()
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
else:
        print("No recipes found.")







    