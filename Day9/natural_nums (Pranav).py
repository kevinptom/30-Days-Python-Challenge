"""
Author - Pranav S Nair
Date - 16/11/2024
Purpose - A python program to print the natural numbers.
"""

limit = int(input("Enter the limit : "))
print(f"The first {limit} natural numbers are")

for i in range(1,limit+1):
    print(i,end = " ")