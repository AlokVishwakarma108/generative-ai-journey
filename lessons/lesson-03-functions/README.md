# Lesson 03 — Functions

## 🎯 Goal
Learn to write reusable, testable blocks of code.

By the end of this lesson you will:
- Create your own functions
- Use parameters and return values
- Understand default arguments

## 🧠 Key Concepts

### 1. Why functions?
- Avoid repetition (DRY — Don't Repeat Yourself)
- Make code readable and testable
- Break big problems into small pieces

### 2. Basic function
```python
def greet():
    print("Hello Alok! Keep learning GenAI.")

greet()      # call the function
```

## Practice Questions

### **Que 1.**
> Create function `add_skill(skill_list, new_skill)` that adds a new skill only if it is not already in the list.

```python
skill = []
def add_skill(skill_list, new_skill):
  if new_skill in skill_list:
    print(f"{new_skill} Skill already exist")
    return False
  else:
    skill_list.append(new_skill)
    return True
```

### **Que 2.**
> Create a function `show_student_info(student_dict) that prints all information of the student nicely.

```python
def show_student_info(student_dict):
   for key, value in student_dict.items():
     print(f"{key} : {value}"")
```

### **Que 3.**
> Implement the both function. <br>
[View File](./example.py)