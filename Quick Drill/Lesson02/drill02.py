'''
Objective: Create a dict me = {"name": "...", "age": ..., "goal": "..."}.
Loop through it and print: key → value
Dev: Alok Vishwakarma
Date: Oct 12, 2026
'''

me = {
  "name" : "Alok Vishwakarma",
  "age" : 21,
  "goal" : "To be a gen AI developer"
}

for key, value in me.items():
  print(f"{key} : {value}")