# Python Recipe App - Career Foundry Specialization

## Project Overview
This is a comprehensive **Command-Line Recipe Application** built in Python throughout Career Foundry's Python Specialization (Achievement 1). The app demonstrates core Python concepts, database management, and object-oriented programming principles.

## Achievements & Exercises

### Achievement 1: Python Fundamentals & Databases

| Exercise | Topic | Skills Covered |
|----------|-------|----------------|
| **1.1** | Hello World & Basic Input/Output | Variables, print(), input() |
| **1.2** | Data Types & Operators | Strings, integers, floats, operators |
| **1.3** | Control Flow & Conditionals | if/elif/else statements |
| **1.4** | Loops & Data Manipulation | for loops, while loops, file handling |
| **1.5** | Object-Oriented Programming | Classes, methods, objects |
| **1.6** | Databases with MySQL | SQL queries, MySQL Connector, CRUD operations |
| **1.7** | ORM with SQLAlchemy | SQLAlchemy ORM, models, sessions |

## Technologies Used

- **Language**: Python 3.x
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Database Connector**: mysql-connector-python, mysqlclient
- **Environment**: Virtual Environment (.venv)

## Project Structure

```
cf_python/
├── 1.1/                          # Exercise 1.1: Basics
│   ├── hello.py
│   ├── add.py
│   └── cf-python-base/          # Virtual environment
├── 1.2/                          # Exercise 1.2: Data types
├── 1.3/                          # Exercise 1.3: Control flow
├── 1.4/                          # Exercise 1.4: Loops
├── 1.5/                          # Exercise 1.5: OOP
│   ├── recipe_oop.py
│   └── Practice/
├── 1.6/                          # Exercise 1.6: Databases
│   ├── recipe_mysql.py
│   └── Practice/
├── 1.7/                          # Exercise 1.7: SQLAlchemy ORM
│   ├── recipe_app.py            # Main application
│   ├── 1.7-Practice_Task_1/     # Practice exercise 1 screenshots
│   ├── 1.7-Practice_Task_2/     # Practice exercise 2 screenshots
│   ├── 1.7-Practice_Task_3/     # Practice exercise 3 screenshots
│   └── Final_App_Screenshots/   # Final app testing screenshots
├── README.md                     # This file
└── Learning Journal.md           # Progress tracking
```

## Installation & Setup

### Prerequisites
- Python 3.x installed
- MySQL Server running locally
- MySQL credentials: username `cf-python`, password `password`
- Database: `task_database` created in MySQL

### Step 1: Navigate to Project
```powershell
cd C:\Users\user\Desktop\Career_Foundry\Specialization\cf_python
```

### Step 2: Activate Virtual Environment
```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies
```powershell
pip install sqlalchemy mysqlclient
```

### Step 4: Run the Recipe App
```powershell
python 1.7\recipe_app.py
```

## Recipe App Features

The final recipe app (`1.7/recipe_app.py`) includes:

1. **Create Recipe** - Add new recipes with name, ingredients, and cooking time
   - Auto-calculates difficulty based on cooking time and ingredient count
   - Validates user input

2. **View All Recipes** - Display all recipes in a formatted table

3. **Search by Ingredients** - Find recipes containing specific ingredients
   - Select multiple ingredients by number
   - Uses SQLAlchemy filter with LIKE operator

4. **Edit Recipe** - Modify existing recipe details
   - Edit name, ingredients, or cooking time
   - Auto-recalculates difficulty

5. **Delete Recipe** - Remove recipes with confirmation

## Database Schema

### Table: `final_recipes`
| Column | Type | Constraints |
|--------|------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT |
| name | VARCHAR(50) | Recipe name |
| ingredients | VARCHAR(255) | Comma-separated ingredients |
| cooking_time | INT | Time in minutes |
| difficulty | VARCHAR(20) | Easy/Medium/Intermediate/Hard |

## Difficulty Calculation Logic

```
IF cooking_time < 10 AND num_ingredients < 4 → Easy
IF cooking_time < 10 AND num_ingredients >= 4 → Medium
IF cooking_time >= 10 AND num_ingredients < 4 → Intermediate
IF cooking_time >= 10 AND num_ingredients >= 4 → Hard
```

## Design Decisions

### Why Dictionary for Recipe (Early Exercises)
I chose a dictionary to store each recipe because it keeps every attribute as a clear key-value pair, making fields like name, cooking_time, and ingredients easy to read and retrieve. Keys give the structure flexibility: I can add new attributes without reshaping existing data. This clarity and adaptability help when editing recipes and when the Recipe app grows.

### Why List for All Recipes (Early Exercises)
I used a list to hold all recipes because a list naturally keeps entries in sequence and supports quick iteration. It lets me append new recipes, remove outdated ones, and loop over the collection for printing or searching without extra overhead. This makes scaling the Recipe app straightforward while keeping code simple and readable.

### Why SQLAlchemy ORM (Exercise 1.7)
SQLAlchemy ORM provides several advantages over raw SQL:
- **Database Agnostic**: Easily switch databases without rewriting queries
- **Object-Oriented**: Work with Python objects instead of SQL strings
- **Type Safety**: Catch errors at development time
- **Less Boilerplate**: No need to write repetitive SQL queries
- **Maintainability**: Cleaner, more readable code

## How to Use the App

1. Start the app: `python 1.7\recipe_app.py`
2. Choose an option from the menu (1-5 or quit)
3. Follow on-screen prompts
4. Invalid inputs are handled with error messages
5. Type `quit` to exit safely

## Practice Exercises Completed

- **Practice 1**: Add 3 recipes (Coffee, Cake, Banana Smoothie) using ORM
- **Practice 2**: Filter recipes containing "Sugar" ingredient
- **Practice 3**: Update Cake recipe with Chocolate Powder

## Testing
All app features have been tested with:
- Valid inputs
- Invalid inputs (error handling)
- Edge cases (empty database, non-existent IDs, etc.)

## Learning Outcomes

Through this specialization, I've learned:
✓ Python fundamentals (variables, data types, operators)
✓ Control flow and loops
✓ Functions and code organization
✓ Object-oriented programming
✓ File handling and persistence
✓ Database design and SQL
✓ ORM concepts and SQLAlchemy
✓ Error handling and input validation
✓ Building complete applications

## Author
Career Foundry Python Specialization - Student Project
