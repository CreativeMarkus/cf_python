# Practice Task 4: Additional ORM Operations

## Objective
Reinforce and expand your understanding of SQLAlchemy ORM with additional database operations and scenarios.

## What You'll Learn
This practice builds on the previous three tasks and prepares you for the main application by exploring:
- Retrieving single records vs multiple records
- Advanced filtering with multiple conditions
- Deleting records
- Using different query methods
- Error handling with database operations

## Practice Exercises

### Exercise 4.1: Using `get()` to Retrieve by Primary Key
```python
# Get a single recipe by its ID (primary key)
tea_recipe = session.query(Recipe).get(1)
print(tea_recipe)
# Output: <Recipe ID: 1-Tea>
```

### Exercise 4.2: Using `one()` with filter()
```python
# Get exactly one result from a filter query
coffee = session.query(Recipe).filter(Recipe.name == 'Coffee').one()
print(coffee)
# Output: <Recipe ID: 2-Coffee>

# Note: .one() throws error if no results or multiple results
```

### Exercise 4.3: Using `first()` for First Result
```python
# Get only the first result from a filter query
first_recipe = session.query(Recipe).filter(Recipe.cooking_time < 10).first()
print(first_recipe)
# Output: <Recipe ID: 1-Tea>
```

### Exercise 4.4: Multiple Conditions with filter()
```python
# Find recipes with specific criteria
results = session.query(Recipe).filter(
    Recipe.cooking_time < 30,
    Recipe.name != 'Tea'
).all()

for recipe in results:
    print(recipe)
```

### Exercise 4.5: Using with_entities() to Select Specific Columns
```python
# Retrieve only specific columns, not entire row
names = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
print(names)
# Output: [(1, 'Tea'), (2, 'Coffee'), (3, 'Cake'), (4, 'Banana Smoothie')]
```

### Exercise 4.6: Count Records
```python
# Count total recipes in database
total = session.query(Recipe).count()
print(f"Total recipes: {total}")
# Output: Total recipes: 4
```

### Exercise 4.7: Delete a Record
```python
# First add a test recipe
test_recipe = Recipe(
    name="Test Recipe",
    ingredients="Test Ingredients",
    cooking_time=10
)
session.add(test_recipe)
session.commit()

# Then delete it
recipe_to_delete = session.query(Recipe).filter(Recipe.name == 'Test Recipe').one()
session.delete(recipe_to_delete)
session.commit()

print("Recipe deleted!")
```

### Exercise 4.8: Update Using .update() Method
```python
# Update multiple records at once (direct database update)
session.query(Recipe).filter(Recipe.name == 'Cake').update({Recipe.name: 'Birthday Cake'})
session.commit()

print("Recipe name updated!")
```

### Exercise 4.9: Handle Errors Gracefully
```python
# Try to get a non-existent recipe
try:
    recipe = session.query(Recipe).get(999)
    if recipe is None:
        print("Recipe not found!")
except Exception as e:
    print(f"Error: {e}")
```

### Exercise 4.10: Order and Limit Results
```python
# Get first 2 recipes ordered by cooking time
results = session.query(Recipe).order_by(Recipe.cooking_time).limit(2).all()

for recipe in results:
    print(f"{recipe.name}: {recipe.cooking_time} mins")
```

## Query Method Comparison

| Method | Returns | Use Case |
|--------|---------|----------|
| `.all()` | List | Get all matching records |
| `.one()` | Single Object | Expect exactly one result |
| `.first()` | Single Object or None | Get first result (or None) |
| `.get(id)` | Single Object or None | Get by primary key |
| `.count()` | Integer | Count matching records |

## Screenshots/Tests to Perform
Document your understanding by testing each exercise:
1. Test `get()` with valid and invalid IDs
2. Test `one()` and see error when no results
3. Test `first()` with filter
4. Test multiple conditions
5. Test `with_entities()` output format
6. Test `count()` at different points
7. Test delete operation and verify deletion
8. Test update and verify change

## Common Patterns Used in Main Application

These exercises prepare you for the main app:
```python
# Pattern 1: Check if records exist
if session.query(Recipe).count() == 0:
    print("No recipes found")

# Pattern 2: List with numbers for user selection
all_recipes = session.query(Recipe).all()
for i, recipe in enumerate(all_recipes, 1):
    print(f"{i}. {recipe.name}")

# Pattern 3: Get by user input
recipe_id = int(input("Enter recipe ID: "))
recipe = session.query(Recipe).get(recipe_id)
if not recipe:
    print("Recipe not found!")

# Pattern 4: Search with multiple conditions
conditions = [Recipe.ingredients.like(f"%{ing}%") for ing in ingredients_list]
results = session.query(Recipe).filter(*conditions).all()
```

## Key Learning Points
✓ Different ways to retrieve records from database
✓ Query methods: `.all()`, `.one()`, `.first()`, `.get()`
✓ Selecting specific columns with `with_entities()`
✓ Counting records efficiently
✓ Deleting records safely
✓ Batch updates with `.update()`
✓ Ordering and limiting results
✓ Error handling for database operations

## Files in This Folder
- `README.md` - This file
- Test results or screenshots (optional)

## Ready for Main Application?
After completing all 4 practice tasks, you should be ready to:
1. Build the complete Recipe App with all CRUD operations
2. Implement the 5 main functions
3. Create the main menu loop
4. Handle user input validation
5. Integrate all ORM concepts

## Next: Main Task
Proceed to `recipe_app.py` to build the complete application using all these concepts!
