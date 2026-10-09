# Lesson 04 — Modules

## 🎯 Goal
Learn to use Python's built-in modules and organize your own code into reusable files.

By the end of this lesson you will:
- Import and use `math`, `random`, `datetime`
- Understand `from X import Y` syntax
- Build a small utility function using a module

## 🧠 Key Concepts

### 1. What is a module?
A **module** is just a `.py` file containing Python code that you can
import into other files. Python ships with hundreds of standard modules.

### 2. Import styles
```python
import math                        # full module
print(math.sqrt(16))

from datetime import datetime      # specific name or Improt Directly Function from Modules
print(datetime.now())

import random as rnd               # alias
print(rnd.randint(1, 10))
```

### 3. Some Common *Maths* Function
| Function | Use | Syntax |
|---|---|---|
| pi | To get the value of pi | `print(math.pi)` |
| sqrt(a) | Calculate the Square Root of a value | `math.sqrt(16)` |
| pow(a, b) | Calculate the power value a^b | `math.pow(2,3)` |
| ceil(float) | Get Next Heighest Integer | `math.ceil(4.2)` |
| floor(4.8) | Get Previous Lowest Integer | `math.floor(4.8)` |
| factorial(a) | Calculate factorial | `math.factorial(5)` |

### 4. Some Common *Random* Module Functions
| Function | Use | Syntax |
|---|---|---|
| randint(a,b) | To Choose Random value from `a` to `b` | `random.randint(1,10)` |
| random() | Generate random value int, floot | `random.random()` |
| choice(list_name) | Select one value from a list | `random.choice(frutes)` |
