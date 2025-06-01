
task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority == "high" and time_bound == "yes":
    print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
elif priority == "high" and time_bound == "no":
    print(f"Reminder: '{task}' is a high priority task: Start planning to work on it!")
elif priority == "low" and time_bound in ["no", "yes"]:
    print(f"Reminder: '{task}' is a low priority task: Consider completing it when you have free time!")
elif priority == "medium" and time_bound in ["yes", "no"]:
    print(f"Reminder: '{task}' is a medium priority task: Consider completing it when you have free time!")
else:
    print("Get busy! Time no dey!")
