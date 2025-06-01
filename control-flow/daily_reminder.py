
task = input("Enter your task: ").strip().lower()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"🔔 Reminder: '{task}' is a **high priority** task that requires **immediate attention today**!")
        else:
            print(f"📝 Reminder: '{task}' is a **high priority** task. Start **planning to work on it**!")
    case "medium":
        print(f"📌 Reminder: '{task}' is a **medium priority** task. Try to complete it **within the week**.")
    case "low":
        print(f"📎 Reminder: '{task}' is a **low priority** task. Handle it when you have **spare time**.")
    case _:
        print("⚠️ Invalid priority. Get busy! Time no dey!")

