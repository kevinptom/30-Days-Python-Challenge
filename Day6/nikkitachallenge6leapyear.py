"""
AUTHOR:Nikkita Anna George
created on:13/11/24
program to check leap year
"""
year=int(input("Enter the year:"))
if (year%4==0 and year %100!=0) or year% 400==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
