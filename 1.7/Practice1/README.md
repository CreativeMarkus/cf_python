# Practice Task 1: Adding Entries to practice_recipes Table Using ORM

## Overview
This folder contains screenshots documenting the completion of Practice Task 1 - adding 3 recipe entries (Coffee, Cake, Banana Smoothie) to the `practice_recipes` table using SQLAlchemy ORM.

## Screenshots Included

### 1. `activation.png`
Shows the activation of the Python virtual environment in PowerShell.
- Command: `.\.venv\Scripts\Activate.ps1`
- Indicator: `(.venv)` appears at the start of the prompt

### 2. `installation.png`
Documents the installation of required packages.
- Packages installed: SQLAlchemy, mysqlclient
- Command: `pip install sqlalchemy mysqlclient`

### 3. `ipython_imports.png`
Shows the importing of necessary SQLAlchemy modules in IPython.
- Imported: `create_engine`, `declarative_base`, `Column`, `Integer`, `String`, `sessionmaker`

### 4. `model.png`
Displays the Recipe model/class definition.
- Shows the SQLAlchemy ORM model structure
- Includes all columns: id, name, ingredients, cooking_time, difficulty
- Shows the `__repr__` method implementation

### 5. `session_data.png`
Documents the creation of Recipe objects and their addition to the database.
- Shows Recipe object creation for Coffee, Cake, and Banana Smoothie
- Shows `session.add()` and `session.commit()` operations
- Verifies all 4 recipes in the table (Tea + 3 new recipes)

### 6. `mysql_check.png`
Confirms the recipes were successfully added to the database via MySQL command line.
- Command: `USE my_database; SELECT * FROM practice_recipes;`
- Shows all 4 recipes with complete details in MySQL table format

## What Was Accomplished

✅ Connected to MySQL database using SQLAlchemy
✅ Created declarative base for ORM models
✅ Defined Recipe class with proper SQLAlchemy columns
✅ Created session object for database transactions
✅ Added 3 new recipes:
   - Coffee (5 min, Coffee Powder/Sugar/Water)
   - Cake (50 min, Sugar/Butter/Eggs/Vanilla Essence/Flour/Baking Powder/Milk)
   - Banana Smoothie (5 min, Bananas/Milk/Peanut Butter/Sugar/Ice Cubes)
✅ Committed changes to database
✅ Verified records both in IPython and MySQL CLI

## Database State After Practice 1

**Table:** `practice_recipes`

| ID | Name | Ingredients | Cooking Time | Difficulty |
|---|---|---|---|---|
| 1 | Tea | Tea Leaves, Water, Sugar | 5 | NULL |
| 2 | Coffee | Coffee Powder, Sugar, Water | 5 | NULL |
| 3 | Cake | Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk | 50 | NULL |
| 4 | Banana Smoothie | Bananas, Milk, Peanut Butter, Sugar, Ice Cubes | 5 | NULL |

## Key Concepts Demonstrated

1. **SQLAlchemy Engine** - Connection bridge to database
2. **Declarative Base** - Foundation for ORM models
3. **ORM Model Definition** - Python class representing database table
4. **Column Types** - Integer, String with constraints
5. **Session Management** - Add, commit, track changes
6. **Object Persistence** - Python objects stored in database
7. **__repr__ Method** - String representation of objects

## Code Pattern Used

```python
# Setup
engine = create_engine("mysql://cf-python:password@localhost/my_database")
Base = declarative_base()

# Model Definition
class Recipe(Base):
    __tablename__ = "practice_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))
    
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"

# Session & Operations
Session = sessionmaker(bind=engine)
session = Session()

coffee = Recipe(name="Coffee", ingredients="Coffee Powder, Sugar, Water", cooking_time=5)
session.add(coffee)
session.commit()
```

## Learning Outcomes

After completing this practice task, you should understand:
- ✓ How to connect to MySQL using SQLAlchemy (not raw connectors)
- ✓ How ORM maps Python classes to database tables
- ✓ How to define models with proper column types
- ✓ How to create session objects for database transactions
- ✓ How to add and commit objects to the database
- ✓ How to verify changes in both Python and MySQL CLI
- ✓ The advantages of ORM over raw SQL queries

## Next Step

Proceed to **Practice Task 2** - Filter recipes by ingredients using the `like()` method.

---

**Completion Date:** January 27, 2026
**Status:** ✅ Complete
