""""
Author:Niya Pius
Date:21/12/24
Python program to find multiplication table of a given number.
"""
num=int(input("Enter the number:"))
for i in range(1,10+1):
    product=num*i
    print(num,"*",i,"=",product)
