'''
Obbjective: Ask the user for their name and daily study hours. Print:
"Alok, you will study 90 hours in 30 days."
Dev: Alok Vishwakarma
Datw: Oct 11, 2026
'''

name = input("Enter Your Name: ")
study_hour_per_day = int(input("How many hours you study per day: "))
print(f"{name}, you will study {study_hour_per_day * 30} hours in 30 days.")

