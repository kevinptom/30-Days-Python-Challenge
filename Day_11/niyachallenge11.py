'''
Author:Niya Pius
Date:21-12-2024
Python program to find the factorial of a given number
Version:1.0
'''
number=int(input("Enter your number:"))
factorial=1
store_num=number
while number>0:
    factorial=factorial*number
    number=number-1
print("The factorial of ",store_num," is :",factorial)
