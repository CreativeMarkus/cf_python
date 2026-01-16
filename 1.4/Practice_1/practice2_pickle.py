import pickle

recipe = {
    "name": "Tea",
    "ingredients": ["Tea leaves", "Water", "Sugar"],
    "time": 5,
    "difficulty": "Easy"
}

with open("recipe_binary.bin", "wb") as file:
    pickle.dump(recipe, file)

with open("recipe_binary.bin", "rb") as file:
    loaded_recipe = pickle.load(file)

print("Recipe Loaded:")
print(loaded_recipe)
