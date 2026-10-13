'''
Objective: Write is_passed(marks) that return True if marks >= 40, else False.

Dev: Alok Vishwakarma
Date: Oct 13, 2026
'''

mm = int(input("Enter your marks: "))
def is_passed(marks):
  if marks >= 40:
    return True
  else:
    return False

print(is_passed(mm))