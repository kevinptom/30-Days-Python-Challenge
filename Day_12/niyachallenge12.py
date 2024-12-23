"""
Author: Niya Pius
Date : 22/12/24
Python program to print sum of natural numbers up to a limit
"""

num = int(input("Enter the limit : "))
original_number = num
sum = 0
while num != 0:
    sum =sum+num
    num = num - 1
print(f"The sum of first {original_number} natural numbers is : {sum}")
