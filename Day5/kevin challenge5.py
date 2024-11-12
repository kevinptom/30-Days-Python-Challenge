'''
Author:Kevin P Tom
Date:12-11-2024
Python program to familiarise string functions
version 1.0
'''
str = input("Orginal Name:")

print(f'Uppercase:{str.upper()}')

print(f'Lowercase:{str.lower()}')

print(f'Title Case:{str.title()}')  #to print the first letter of each word in capital
str1 = str.replace(' ','')
print(f'Total Characters(excluding spaces):{len(str)}')  #to print the length of string
