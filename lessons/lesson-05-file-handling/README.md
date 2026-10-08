# Lesson 05 — File Handling + Error Handling

## 🎯 Goal
Learn to save and read data from files, and to handle errors gracefully.

By the end of this lesson you will:
- Create, write, and read text files
- Understand `"r"`, `"w"`, `"a"` modes
- Use `try-except` to catch errors

## 🧠 Key Concepts

### 1. Why files matter in AI
- Save training logs
- Cache embeddings and results
- Store prompts, configs, and datasets
- Load checkpoints (later with PyTorch)

### 2. Writing to a file
```python
with open("progress.txt", "w") as file:    # "w" = overwrite
    file.write("Alok is learning Generative AI\n")
    file.write("Completed Lesson 5\n")

### 2.1. Reading a file
```python
with open("progress.txt", "r") as file:    # "r" = read
    content = file.read()
    print(content)

### 2.2. Appending to a file
```python
with open("progress.txt", "a") as file:    # "a" = append
    file.write("Completed Lesson 6\n")


### 3. File Modes cheat sheet

| Mode | Meaning |
| r | read (default, error if missing) |
| w | write (overwrites file) |
| a | append (adds to end) |
| r+ | read + write |
| rb | read binary (images, weights)|

### **Note** : The with statement automatically closes the file even if an error occurs. Never use open() without with in production code.

## Error Handling

### Built-in Exception types --

