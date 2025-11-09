"""
Create a Python script that asks the user for their
current age and then calculates how old
they will be in a specific future year.
This task introduces handling
user input and reinforces arithmetic operations.
"""

Age = int(input("How old are you? : "))
current_year = 2025
birth_year = (current_year - Age)
future_year = 2050
future_age = (future_year - birth_year)
print("In 2050, you will be ", future_age, " years old")