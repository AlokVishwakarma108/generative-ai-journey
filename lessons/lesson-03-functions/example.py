"""
Lesson 03 — Functions
"""

def calculate_study_time(days, hours_per_day):
    """Return total hours studied over given days."""
    return days * hours_per_day

def check_commitment(hours):
    """Return commitment level based on daily study hours."""
    if hours >= 3:
        return "Excellent commitment"
    elif hours >= 1:
        return "Good, can improve"
    return "Need more consistency"

def student_progress(name, completed, total):
    progress = (completed / total) * 100
    print(f"Student: {name} | Progress: {progress:.1f}%")
    if progress >= 50:
        return "Strong Progress!"
    elif progress >= 25:
        return "Building Momentum!"
    return "Just Started. Keep going!"

# Test
total = calculate_study_time(30, 3)
message = check_commitment(3)
status = student_progress("Alok Vishwakarma", 5, 40)

print(f"After 30 days: {total} hours")
print("Commitment:", message)
print("Status:", status)
