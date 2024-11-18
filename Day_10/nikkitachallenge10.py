""""
author:Nikkita Anna George
created on:18/11/24
program to find multiplication table of inputted number.
"""
number=int(input("Enter the number:"))
for i in range(1,10+1):
    product=number*i
    print(number,"*",i,"=",product)