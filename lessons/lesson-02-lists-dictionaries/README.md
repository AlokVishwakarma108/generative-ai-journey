
---

## 📄 `lessons/lesson-02-lists-dictionaries/README.md`

```markdown
# Lesson 02 — Lists, Dictionaries & Control Flow

## 🎯 Goal
Learn the two data structures you will use *everywhere* in AI code,
and how to control the flow of your programs.

By the end of this lesson you will:
- Use lists for datasets and sequences
- Use dictionaries for configs and structured data
- Write `if/elif/else`, `for`, and `while` blocks

## 🧠 Key Concepts

### 1. Lists
Ordered, changeable collections.
```python
skills = ["Python", "Maths", "Data Analysis"]
skills.append("TensorFlow")     # add to end
skills[0]                       # first item
skills[-1]                      # last item
skills[1:3]                     # slice
len(skills)                     # length
"Python" in skills              # membership test → True
