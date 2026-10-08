
---

## 📄 `lessons/lesson-04-modules/README.md`

```markdown
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

from datetime import datetime      # specific name
print(datetime.now())

import random as rnd               # alias
print(rnd.randint(1, 10))
