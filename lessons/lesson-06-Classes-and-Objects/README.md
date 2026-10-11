# Lesson 06 — Classes And Objects (OOPs)

## What is a Class? What is an Object?
- Class = Blueprint like a recipe
- Object = Actual thing built from that blueprint like Dish

```python
class Student:
  pass

st1 = Student()
print(type(st1))
print(Student())
```

> *Explaination :*
> - `class Student` defines a blueprint for a student object.
> - The `pass` is used to because the class is empty, so it used as placeholder.
> - `st1 = Student()` : `st1` is an instance of student class
> - the `Student()` class is the blueprint to creating the student object while `st1` is a specific instance created from it.
 
## `__init__` and self