"""
Author - Pranav S Nair
Date - 15/11/2024
Purpose - A python program to print the smallest of three numbers.
"""

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if (num1 <= num2 and num2 <= num3):
    print(f"{num1} is the smallest.")
elif(num2 <= num1 and num2 <= num3):
    print(f"{num2} is the smallest.")
else:
    print(f"{num3} is the smallest.")