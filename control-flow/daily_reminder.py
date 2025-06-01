# daily_reminder.py

# Prompt for task description
task = input("Enter your task: ")

# Prompt for task priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt for time sensitivity
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder variable
reminder = ""

# Use match-case for priority-based response
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unrecognized priority."

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if priority in ["high", "medium", "low"]:
        reminder += ". Consider completing it when you have time."

# Print the final reminder message
print("Reminder:", reminder)

