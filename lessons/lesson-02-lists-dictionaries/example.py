"""
Lesson 02 — Lists, Dictionaries & Control Flow
"""

# ---------- LISTS ----------
skills = ["Python", "Maths", "Data Analysis"]
skills.append("PyNum")
skills.append("TensorFlow")
print("Skills:", skills)
print("First:", skills[0], "| Last:", skills[-1])
print("Slice [1:3]:", skills[1:3])

# ---------- DICTIONARIES ----------
me = {
    "name": "Alok Vishwakarma",
    "age": 21,
    "city": "Deoria",
    "goal": "Full stack developer with GenAI skill",
    "skills": skills,
    "daily_study_hour": 3
}

for key, value in me.items():
    print(f"{key}: {value}")

# ---------- CONTROL FLOW ----------
if me["daily_study_hour"] >= 3:
    print("✅ Excellent commitment")
elif me["daily_study_hour"] >= 1:
    print("🟡 Good, can improve")
else:
    print("🔴 Need more consistency")

# ---------- LOOP ----------
print("\nMy Skills:")
for i, skill in enumerate(skills, start=1):
    print(f"{i}. {skill}")
