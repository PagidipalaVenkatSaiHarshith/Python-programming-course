# -*- coding: utf-8 -*-
"""Day01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X3A_eWPheclDlbmHuzEMLprDF3ZBn2Go

##Slide 7: Basic Syntax
"""

# Print statements
print("Hello, World!")
print("Python is fun!")

# Comments
# This is a single-line comment
# hello world

"""jhkfdsjhk
jkfds
"""

"""
This is a multi-line comment
that spans multiple lines
"""

print("Comments are useful for documentation.")

# Arithmetic operations
print(5 + 3)    # Addition
print(10 - 2)   # Subtraction
print(4 * 7)    # Multiplication
print(8 / 2)    # Division

+,-,*, /, %

"""##Slide 8: Variables and Data Types


"""

name = "Alice"
age = 25
height = 5.5
is_student = True

print(name)
print(age)
print(height)
print(is_student)

name = 5
print(name)

"""###Explanation:
* Variables: Containers for storing data values.
* Data Types: int (integer), float (floating-point number), str (string), bool (boolean).

##Slide 8: Input and Output
"""

user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")

"""###Explanation:
* input(): Function to take input from the user.
* print(): Function to display output.

##Day 1 Coding Problems

###Hello, World!
Problem: Write a program that prints "Hello, World!".
"""

print("Hello, World!")

"""###Basic Arithmetic
Problem: Write a program that performs basic arithmetic operations (addition, subtraction, multiplication, division) and prints the results.

"""

print(10 + 5)   # Addition
print(10 - 5)   # Subtraction
print(10 * 5)   # Multiplication
print(10 / 5)   # Division

"""###Variable Assignment
Problem: Write a program that assigns values to variables and prints them.
"""

name = "Alice"
age = 25
height = 5.5
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

"""###User Input
Problem: Write a program that asks the user for their name and greets them.
"""

user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")

"""###Simple Calculator
Problem: Write a program that takes two numbers as input from the user and performs addition, subtraction, multiplication, and division on them. Print the results.
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)