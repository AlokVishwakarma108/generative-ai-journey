"""
Lesson 04 — Modules
"""

import math
import random
from datetime import datetime

print("sqrt(16):", math.sqrt(16))
print("Random 1-10:", random.randint(1, 10))
print("Now:", datetime.now())

# ---------- Study Plan Generator ----------
def generate_study_plan(skills, days=7):
    plan = {}
    for i in range(1, days + 1):
        plan[f"Day {i}"] = random.choice(skills)
    return plan

my_skills = ["Python", "Maths", "ML", "Deep Learning", "Transformers"]
plan = generate_study_plan(my_skills)

print("\n📅 Weekly Plan:")
for day, topic in plan.items():
    print(f"  {day}: {topic}")

# ---------- Skill Manager ----------
def add_skill(skill_list, new_skill):
    if new_skill in skill_list:
        print(f"'{new_skill}' already exists")
        return False
    skill_list.append(new_skill)
    print(f"'{new_skill}' added successfully")
    return True

def show_student_info(student_dict):
    print("\n----- Student Info -----")
    for key, value in student_dict.items():
        print(f"{key.capitalize()}: {value}")

student = {"name": "Alok Vishwakarma", "branch": "CSE", "skills": []}
add_skill(student["skills"], "Python")
add_skill(student["skills"], "Python")   # duplicate test
add_skill(student["skills"], "Machine Learning")
show_student_info(student)
