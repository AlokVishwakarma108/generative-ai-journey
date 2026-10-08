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
