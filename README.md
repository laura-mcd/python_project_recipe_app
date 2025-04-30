Title: 
Ingredient-based Recipe Generator

Description: 
It is a common problem to figure out what is for dinner when looking at a refrigerator and pantry full of ingredients but lack guidance on what to do with them. Through the recipe generator, a user can receive up to ten recipes based on ingredients they have on hand or wish to cook with. Recipe links will be provided along with lists of missing ingredients. 

Data Design:
The API is pulled from Spoonacular API (https://spoonacular.com/food-api) with a “search recipes by ingredients” filter. The API is delivered in JSON format. Creation of a free account is required to obtain an API access key.

Interface Design: 
The API access key is defined within the code but can be edited to include a user’s unique key. The user will need to have a successful request to the API and if not, they will be able to input recipes. Users will receive messages informing them about errors if no recipes are found or if incorrect values are entered.

Component Design: 
Functions- find_recipes uses the API key, its url, and parameters to pull recipes from the API. display_recipes prints the information pulled from the API for the user including the recipe title, the link, and missing ingredients.

Algorithm- the index variable begins at 0 and can max out at 10, meaning 1 to 10 recipes can be returned to the user. The index number increases with each user request to print another recipe. This is done through the notation, “index =+ 1”.

Input specifications- users need to input their ingredients with commas separating each item. If a user enters an ingredient with multiple words, for example “bell pepper”, through a join method, multiple words will be read as single ingredients. When prompted to print another recipe, the user can only input a “y” for yes, print another recipe, or “n” for no, close the program.

Output specifications- recipe links are given with recipe IDs instead of recipe titles. The missing ingredients will be presented as a list separated by commas. Most outputs are given with a description of what is being printed followed by a comma and the information from the API.

User Interface:
Possible workflow- Welcome screen > request ingredients from user > present recipe with button to view another recipe > present recipes until user clicks button to exit > closing screen

Accessibility considerations- ability to change text size, ability for user to increase or decrease contrast, text-to-speech controls

Assumptions and Dependencies:
It is assumed the user is using a windows or mac device to process code in Visual Studio Code.
The free API can only process 150 free pulls each day. Any number of pulls over 150 will cost $0.005 per request. 

How to use the app:
•	You will be greeted and prompted to input ingredients
•	Enter ingredients separated by commas
o	Be sure to specify if ingredients are diet-specific (ex. Gluten-free flour, vegan butter)
o	Diet-specific ingredients will produce compliant recipes
•	A recipe will be pulled via the API and you will be given a recipe title, link to the webpage, and remaining ingredients needed 
•	You will be asked if you want to receive another recipe. Type in “y” for yes and “n” for no.
•	If you replied “y”, you’ll receive another recipe as well as the same option to see an additional recipe.
•	If you replied “n”, the app will close and you can get cooking!

# python_project_recipe_app
