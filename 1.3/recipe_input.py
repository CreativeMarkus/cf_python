import pickle

def calc_difficulty(time, ingredients):
    if time < 10 and len(ingredients) < 4:
        return "Easy"
    elif time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"

def take_recipe():
    name = input("Enter recipe name: ")
    time = int(input("Enter cooking time (minutes): "))
    ingredients = input("Enter ingredients separated by commas: ").split(",")

    ingredients = [item.strip() for item in ingredients]
    difficulty = calc_difficulty(time, ingredients)

    recipe = {
        "name": name,
        "time": time,
        "ingredients": ingredients,
        "difficulty": difficulty
    }

    return recipe

filename = input("Enter filename to store recipes: ")

try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    data = {"recipes_list": [], "all_ingredients": []}
except:
    data = {"recipes_list": [], "all_ingredients": []}
else:
    file.close()
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]

num = int(input("How many recipes would you like to enter? "))

for _ in range(num):
    recipe = take_recipe()
    recipes_list.append(recipe)

    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

data = {
    "recipes_list": recipes_list,
    "all_ingredients": all_ingredients
}

with open(filename, "wb") as file:
    pickle.dump(data, file)

print("Recipes saved successfully!")
