"""
Task Description:

Develop a script named daily_reminder.py. This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.

Instructions:

Prompt for a Single Task:

Ask the user to input a task description and save it into a task variable
Prompt for the task’s priority (high, medium, low) and save it into a priority variable
In a time_bound variable, Ask if the task is time-bound (yes or no)
Process the Task Based on Priority and Time Sensitivity:

Use a Match Case statement to react differently based on the task’s priority.
Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
Provide a Customized Reminder:

Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
A message should be ‘that requires immediate attention today!’

"""
# user input for task description
task = input("Enter your task: ")
# user input for task priority
priority = input("priority (high/medium/low): ")
# user input for time sensitivity
time_bound = input("Is this task time-bound? (yes/no): ")
# using match case to provide reminder based on priority
match priority.lower():
    case "high":
        reminder = f"Reminder:'{task}' is a high-priority task  requires immediate attention today!"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium-priority task  should be addressed soon."
    case "low":
        reminder = f"Reminder: '{task}' is a low-priority task  can be handled at your convenience."
    case _:
        reminder = f"Reminder: '{task}' is task  has an unrecognized priority level."
print(reminder)
