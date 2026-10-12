'''
Objective: Write an if-elif-else that prints:

· "Excellent" if hours ≥ 3
· "Good" if hours ≥ 1
· "Need more" otherwise

Test with 3 different values.
Dev: Alok Vishwakarma
Date: Oct 12, 2026
'''

study_hours = int(input("Study hours par day: "))
if study_hours >= 3:
  print("Excellent")
elif study_hours >= 1:
  print("Good")
else:
  print("Need more")
  