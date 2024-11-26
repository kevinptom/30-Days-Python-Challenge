""""
Author: Pranav S Nair
Date : 26/11/24
A python program to print sum of natural numbers using while loop
"""

num = int(input("Enter the limit : "))
original_num = num
sum = 0
while num != 0:
    sum += num
    num = num - 1
print(f"The sum of first {original_num} natural numbers is : {sum}")


