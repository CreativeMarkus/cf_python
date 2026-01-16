import pickle

def display_recipe(recipe):
    print("\n----------------------")
    print("Recipe:", recipe["name"])
    print("Cooking Time:", recipe["time"], "minutes")
    print("Ingredients:", ", ".join(recipe["ingredients"]))
    print("Difficulty:", recipe["difficulty"])

def search_ingredient(data):
    print("\nAvailable Ingredients:")
    for index, ingredient in enumerate(data["all_ingredients"]):
        print(index, ingredient)

    try:
        choice = int(input("Select ingredient number: "))
        ingredient_searched = data["all_ingredients"][choice]
    except:
        print("Invalid input.")
        return
    else:
        print(f"\nRecipes containing {ingredient_searched}:")
        for recipe in data["recipes_list"]:
            if ingredient_searched in recipe["ingredients"]:
                display_recipe(recipe)

filename = input("Enter recipe file name: ")

try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
except:
    print("File not found.")
else:
    search_ingredient(data)
