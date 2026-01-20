import mysql.connector

conn = mysql.connector.connect(host='localhost', user='cf-python', passwd='password')
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)''')

def calculate_difficulty(cooking_time, ingredients):
    num_ingredients = len(ingredients.split(','))
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"

def create_recipe():
    name = input("Recipe name: ")
    cooking_time = int(input("Cooking time (mins): "))
    ingredients = input("Ingredients (comma-separated): ")
    difficulty = calculate_difficulty(cooking_time, ingredients)
    
    query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, ingredients, cooking_time, difficulty))
    conn.commit()
    print("Recipe added!")

def search_recipe():
    cursor.execute("SELECT DISTINCT ingredients FROM Recipes")
    results = cursor.fetchall()
    all_ingredients = set()
    for row in results:
        for ing in row[0].split(','):
            all_ingredients.add(ing.strip())
    
    print("\nIngredients:", list(all_ingredients))
    search = input("Ingredient to search for: ")
    query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(query, ('%' + search + '%',))
    for row in cursor.fetchall():
        print(row)

def update_recipe():
    cursor.execute("SELECT id, name FROM Recipes")
    for row in cursor.fetchall(): print(f"ID: {row[0]} | Name: {row[1]}")
    recipe_id = input("ID to update: ")
    column = input("Update name, cooking_time, or ingredients? ")
    new_value = input("New value: ")
    
    query = f"UPDATE Recipes SET {column} = %s WHERE id = %s"
    cursor.execute(query, (new_value, recipe_id))
    
    # Recalculate difficulty
    cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (recipe_id,))
    res = cursor.fetchone()
    new_diff = calculate_difficulty(res[0], res[1])
    cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (new_diff, recipe_id))
    conn.commit()
    print("Recipe updated!")

def delete_recipe():
    cursor.execute("SELECT id, name FROM Recipes")
    for row in cursor.fetchall(): print(row)
    recipe_id = input("ID to delete: ")
    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
    conn.commit()
    print("Recipe deleted!")

def main_menu():
    choice = ""
    while choice != 'quit':
        print("\n1. Create | 2. Search | 3. Update | 4. Delete | quit to exit")
        choice = input("Choice: ").lower()
        if choice == '1': create_recipe()
        elif choice == '2': search_recipe()
        elif choice == '3': update_recipe()
        elif choice == '4': delete_recipe()

if __name__ == "__main__":
    main_menu()
    conn.close()