# Lesson 06 — Object Oriented Programming

## 🧠 What I Learned (in my own words)

OOP is just a way to make a **blueprint** once, then create many copies
from it. Instead of writing name, age, goal for every student again and
again, I write one "Student blueprint" and stamp out students from it.

- **Class** = the blueprint (recipe)
- **Object** = the actual thing made from the blueprint (the dish)

Example:
- `class Student:` is the blueprint
- `alok = Student("Alok", 21)` is an object

Same blueprint, different data. That's the whole point.

---

## 🧠 `__init__` — runs automatically

`__init__` is a special function that runs **by itself** when I create
an object. It's used to set up the object's data (name, age, etc.).

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

When I write `Student("Alok", 21)`, Python secretly does:
`Student.__init__(alok, "Alok", 21)`

So `self` = the object being created. Nothing magical.

---

🧠 self — finally understood

self means "THIS object I'm working on right now."

```python
alok = Student("Alok", 21)
priya = Student("Priya", 22)
```

Inside the class:
- `self.name = name` — for alok, becomes `alok.name = "Alok"`
- For priya, the same line becomes `priya.name = "Priya"`

Same code. Different object. self just points to whichever object is being used.

Rule I will remember:

self is the object. When calling a method, I don't pass it — Python passes it for me.

---

### 🧠 Methods — functions inside a class

A method is a function that lives inside a class and uses self.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old.")

alok = Student("Alok", 21)
alok.introduce()    # Hi, I'm Alok, 21 years old.
```

Notice: I wrote `alok.introduce()` — NOT `alok.introduce(alok)`. Python handles self automatically.

---

## 🧠 `__str__` — clean printing

By default, `print(alok)` shows something ugly like `<Student object at 0x7f...>`.
I can fix that with `__str__`.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student({self.name}, {self.age})"

print(Student("Alok", 21))    # Student(Alok, 21)
```

`__str__` just tells Python: "when someone prints me, show this instead."

---

🧠 Why OOP matters for AI (this clicked for me)

When I saw PyTorch code like this:

```python
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Linear(10, 5)

    def forward(self, x):
        return self.layer(x)
```

...I realized — it's the same thing I just learned!

| What I learned | How PyTorch uses it|
|---|---|
| class Student: | class MyModel(nn.Module): |
| def __init__(self): | def __init__(self): |
| self.name = name | self.layer = nn.Linear(...) |
| def introduce(self): | def forward(self, x): |
| Student("Alok", 21) | MyModel() |

OOP is not extra theory. It IS AI code.

---

💻 My Practice Code [Practice File](./example.py)

---

📝 My Notes in One Line

A class is a blueprint. An object is one thing made from it.
self = the current object. `__init__` runs on creation.
`__str__` controls printing. And every AI framework is built on this.

---

❓ What I Understanding

1. What is a class?
   A blueprint used to create objects.
2. What is an object?
   One actual thing made from the class.
3. What does self mean?
   The object the method is currently working on.
4. What does `__init__` do?
   Runs automatically when an object is created, sets its attributes.
5. What is `__str__` for?
   Controls how the object looks when printed.
