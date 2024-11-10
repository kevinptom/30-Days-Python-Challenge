"""
Author - Pranav S Nair
Date - 10/11/2024
Purpose - [Day 3] - To understand the concept of arithmetic operators
Version - 1.0
""" 

num1 = float(input("Enter 1st number : "))
num2 = float(input("Enter 2nd number : "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
floor_division = num1 // num2

print(f"The sum of {num1} and {num2} is {addition}.")
print(f"The difference when {num2} is subtracted from {num1} is {subtraction}.")
print(f"The product of {num1} and {num2} is {multiplication}.")
print(f"The quotient of {num1} divided by {num2} is {division}.")
print(f"The remainder when {num1} is divided by {num2} is {modulus}.")
print(f"The integer quotient when {num1} is divided by {num2} is {floor_division}.")
