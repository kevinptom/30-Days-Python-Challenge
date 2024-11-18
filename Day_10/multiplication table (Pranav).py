"""
Author - Pranav S Nair
Date - 18/11/2024
Purpose - A Python program that prints the multiplication table of a inputted number.
"""
num = int(input("Enter the number : "))
print("\nThe multiplication table of",num)

for i in range(1,10+1):
    product = num * i 
    print(f"{num} x {i} = {product}")