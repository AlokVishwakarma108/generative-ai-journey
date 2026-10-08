"""
Lesson 05 — File Handling + Error Handling
"""

def save_progress(name, lesson):
    with open("my_progress.txt", "a") as file:
        file.write(f"{name} completed Lesson {lesson}\n")
    print("✅ Progress saved.")

def show_progress():
    try:
        with open("my_progress.txt", "r") as file:
            print("\n--- Your Progress ---")
            print(file.read())
    except FileNotFoundError:
        print("⚠️ No progress file found yet.")

def save_skills(skills_list, filename="skills.txt"):
    with open(filename, "w") as file:
        for skill in skills_list:
            file.write(f"{skill}\n")
    print(f"✅ {len(skills_list)} skills saved to {filename}")

def load_skills(filename="skills.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("⚠️ File not found.")
        return []

# Test
save_progress("Alok Vishwakarma", 5)
save_skills(["Python", "Maths", "ML", "Deep Learning"])
show_progress()
print("Loaded skills:", load_skills())
