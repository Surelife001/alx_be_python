"""
Create a Python script named multiplication_table.py.
 This script will ask the user to enter a number,
   then use a for loop to print the multiplication table
 for that number from 1 to 10.
"""

# user input for the number
number = int(input("Enter a number to see its multiplication table: "))
# using for loop to print multiplication table
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")