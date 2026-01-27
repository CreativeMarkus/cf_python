# Practice Task 3: Update Recipe Attributes Without Committing

## Objective
Learn how to retrieve records from the database, modify their attributes in memory, and understand the difference between uncommitted changes and permanent database modifications.

## What You'll Do
Update the Cake recipe by adding "Chocolate Powder" to its ingredients list, then view the change without committing it to the database (as per instructions).

## Key Concepts
- Retrieving objects from the database
- Modifying object attributes in Python
- Understanding session state (dirty vs clean)
- The difference between uncommitted vs committed changes
- String concatenation with `+=` operator
- When to use `session.commit()` and when not to

## Steps to Complete

### 1. Setup (Same as Previous Practices)
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://cf-python:password@localhost/my_database")
Base = declarative_base()

class Recipe(Base):
    __tablename__ = "practice_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))
    
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"

Session = sessionmaker(bind=engine)
session = Session()
```

### 2. Retrieve All Recipes
```python
# Get all recipes as a list of objects
recipes_list = session.query(Recipe).all()

# Print to see all recipes
print(recipes_list)
```

### 3. Show Original Cake Ingredients
```python
# Cake should be at index 2 (after Tea at 0, Coffee at 1)
print("Original ingredients:")
print(recipes_list[2].ingredients)
# Output: Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk
```

### 4. Add Chocolate Powder
```python
# Append Chocolate Powder to the ingredients string
recipes_list[2].ingredients += ", Chocolate Powder"
```

### 5. Show Updated Ingredients
```python
# Display the updated ingredients
print("Updated ingredients:")
print(recipes_list[2].ingredients)
# Output: Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk, Chocolate Powder
```

### 6. DO NOT COMMIT
```python
# As per instructions: Do NOT run session.commit()
# This keeps the change in memory only, not in the database
```

## Understanding Session State

### Uncommitted Changes (This Practice)
- Changes only exist in Python memory
- If you close session without commit, changes are lost
- Database remains unchanged

### Committed Changes (Later Exercises)
- Changes are written to database permanently
- All users can see the changes
- Changes survive session closure

## Example: Before vs After

**Before:**
```
Cake ingredients: Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk
```

**After (without commit):**
```
Cake ingredients: Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk, Chocolate Powder
```

**In database (still unchanged):**
```
SELECT * FROM practice_recipes WHERE id = 3;
# Still shows: Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk
```

## Screenshots to Take
1. **IPython output** showing:
   - Original Cake ingredients before update
   - Updated Cake ingredients after adding Chocolate Powder
   - Name: `Practice3_UpdateCake.png`

## Key Learning Points
✓ How to retrieve objects from database using queries
✓ Python objects are modifiable after retrieval
✓ Session tracks changes to objects (dirty state)
✓ `session.commit()` makes changes permanent
✓ Uncommitted changes are lost if session closes
✓ Difference between in-memory changes and database changes

## Common Mistakes to Avoid
- Accidentally committing when you shouldn't
- Not understanding that index might be different (Tea=0, Coffee=1, Cake=2)
- Assuming database changes without commit (it doesn't!)
- Forgetting the ", " (comma and space) when concatenating ingredients

## Important Note
This practice intentionally does NOT commit changes to teach you:
1. Changes can be made to objects without affecting the database
2. You have control over when to persist changes
3. You can abandon changes by closing session without commit

## Files in This Folder
- `Practice3_UpdateCake.png` - Screenshot showing before and after ingredients
- `README.md` - This file

## Next Steps
After completing this practice:
- Move to Practice 4 or the main task
- In the main task, you'll use `calculate_difficulty()` similar to this update pattern
- Learn other update methods like `session.query().update()`
