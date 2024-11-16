'''
Author:Kevin P Tom
Date:15-11-2024
Python program to  find the laergest of three numbers
version 1.0
'''

num1 = int(input("Enter thr first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if(num1<num2 and num1<num2):
    print(f"The smallest number is:{num1}")
elif(num2<num1 and num2<num3):
    print(f"The smallest number is:{num2}")
else:
    print(f"The smallest number is:{num3}")