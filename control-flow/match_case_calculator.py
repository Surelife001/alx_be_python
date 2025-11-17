"""
Develop a Python script named match_case_calculator.py.
This calculator will prompt the user to enter two numbers
and select an operation (addition, subtraction,
multiplication, or division). The script will then perform 
the selected operation
using a Match Case statement and display the result.
"""


# user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# user input for operation
operation = input(" Choose the operation (+, -, *, /): ")
# using match case to perform the selected operation
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.") 
        else:
            result = num1 / num2
            print(f"The result is {result}")
