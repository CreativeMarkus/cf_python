# Practice Task 2: Filter Recipes by Ingredients Using like() Method

## Objective
Learn how to search for records in a database using SQLAlchemy's `filter()` and `like()` methods to find recipes containing specific ingredients.

## What You'll Do
Use SQLAlchemy ORM to retrieve all recipes that contain "Sugar" in their ingredients list using the `like()` method.

## Key Concepts
- Using `session.query()` to retrieve records
- The `filter()` method - equivalent to SQL WHERE clause
- The `like()` method - equivalent to SQL LIKE operator
- Wildcard patterns: `%` matches any characters
- Method chaining: `query().filter().all()`

## Steps to Complete

### 1. Setup (Same as Practice 1)
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

### 2. Filter Recipes with Sugar
```python
# Using like() to find "Sugar" anywhere in ingredients column
sugar_recipes = session.query(Recipe).filter(Recipe.ingredients.like("%Sugar%")).all()

print(sugar_recipes)
```

### 3. Display Results
```python
# Show each recipe with Sugar
for recipe in sugar_recipes:
    print(recipe)
```

## The LIKE Pattern Explained
- `%Sugar%` - Finds "Sugar" anywhere in the string (before or after)
- `Sugar%` - Finds "Sugar" at the beginning
- `%Sugar` - Finds "Sugar" at the end
- `%ugar%` - Case-insensitive partial match

## Expected Output
The query should return recipes containing "Sugar":
- Tea (Tea Leaves, Water, Sugar)
- Coffee (Coffee Powder, Sugar, Water)
- Cake (contains Sugar)
- Banana Smoothie (contains Sugar)

Should show 3-4 recipes depending on existing data.

## Multiple Conditions Example
To find recipes with BOTH Milk AND Baking Powder:
```python
conditions = [
    Recipe.ingredients.like("%Milk%"),
    Recipe.ingredients.like("%Baking Powder%")
]
results = session.query(Recipe).filter(*conditions).all()
# This unpacks the list with * operator
```

## Screenshots to Take
1. **IPython output** showing filtered results for recipes containing Sugar
   - Name: `Practice2_SugarRecipes.png`

## Key Learning Points
✓ Difference between `all()`, `one()`, `first()`, `get()` methods
✓ How to use `filter()` for WHERE-like conditions
✓ How `like()` works for pattern matching
✓ Method chaining in SQLAlchemy queries
✓ Unpacking lists into function arguments with `*`

## Common Mistakes to Avoid
- Forgetting `%` wildcards in like() pattern
- Not calling `.all()` after `filter()` (it returns a Query object)
- Case sensitivity issues (SQL LIKE is case-insensitive in MySQL)
- Forgetting to use `*` when unpacking conditions list

## Files in This Folder
- `Practice2_SugarRecipes.png` - Screenshot of filtered results
- `README.md` - This file

## Next Steps
After completing this practice:
- Try filtering by other ingredients
- Try using multiple conditions with `filter(*conditions)`
- Move to Practice 3: Update operations
