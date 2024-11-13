"""
Author - Pranav S Nair
Date - 13/11/2024
Purpose - (Day 6) To find if a year is leap year or not
Version - 1.0
"""

year = int(input("Enter the year : "))

if(year%4==0):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")