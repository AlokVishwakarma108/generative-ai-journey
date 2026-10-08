# Lesson 01 — Python Basics for AI

## 🎯 Goal
Set up your Python environment and understand the building blocks of Python
that you will use every day as a GenAI Developer.

By the end of this lesson you will:
- Have a working Python + Jupyter/Colab environment
- Understand variables, data types, and basic operations
- Write and run your first AI-related program

## 🧠 Key Concepts

### 1. Data Types (the foundation)
| Type    | Example        | Where you'll see it in AI              |
|---------|----------------|----------------------------------------|
| `str`   | `"hello"`      | Prompts, tokens, labels                |
| `int`   | `25`           | Epochs, steps, token counts            |
| `float` | `5.9`          | Loss, learning rate, accuracy          |
| `bool`  | `True`         | Flags, conditions                      |
| `list`  | `[1, 2, 3]`    | Datasets, embeddings, batches          |

### 2. Operators
| Operator | Meaning          | Example     |
|----------|------------------|-------------|
| `+`      | addition         | `10 + 3`    |
| `-`      | subtraction      | `10 - 3`    |
| `*`      | multiplication   | `10 * 3`    |
| `/`      | division         | `10 / 3`    |
| `//`     | floor division   | `10 // 3` → 3 |
| `%`      | remainder        | `10 % 3` → 1  |
| `**`     | power            | `10 ** 3` → 1000 |

### 3. Strings
```python
message = "I will become a Generative AI Developer"
message.upper()       # uppercase
message.lower()       # lowercase
len(message)          # length
message[0:5]          # slice → "I wil"
