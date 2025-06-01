# daily_reminder.py

# Prompt user for task description
task = input("Enter your task: ")

# Prompt user for priority level
priority = input("Priority (high/medium/low): ").lower()

# Prompt user if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match case to respond based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Task priority '{priority}' is not recognized."

# Modify reminder based on time sensitivity
if time_bound == "yes":
    if priority in ["high", "medium"]:
        reminder += " that requires immediate attention today!"
    elif priority == "low":
        reminder += ". Even though it's low priority, it requires immediate attention today!"
else:
    if priority in ["high", "medium"]:
        reminder += ". Please plan to complete it soon."
    elif priority == "low":
        reminder += ". Consider completing it when you have free time."

print(reminder)
