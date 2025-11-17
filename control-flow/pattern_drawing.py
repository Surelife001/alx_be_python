"""
Develop a Python script named pattern_drawing.py. This script will prompt
 the user to enter a positive integer,
 then use nested loops to print a square pattern of that size made of asterisks (*).
"""

# user input for the size of the square pattern
size = int(input("Enter the size of the pattern: "))
# using nested loops to print the square pattern
for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()  # move to the next line after each row