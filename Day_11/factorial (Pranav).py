"""
Author - Pranav S Nair
Date - 20/11/2024
A python program to print the factorial of a number 
"""

num = int(input("Enter the number : "))
factorial = 1                          #initialising the variable 'factorial'
store_num = num                        #storing the input to display it later 

while num>0:
    factorial *= num
    num -= 1

print(f"The factorial of the {store_num} is {factorial}")