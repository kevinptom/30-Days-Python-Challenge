"""
Author - Pranav S Nair
Date - 12/11/2024
Purpose - To familiarize with basic string functions part 2
"""

full_name = input("Enter a full name : ")
full_name_without_spaces = full_name.replace(" ","")
print("Uppercase:",full_name.upper())
print("Lowercase:",full_name.lower())
print("Test Case:",full_name.title())
length_of_fullname = len(full_name_without_spaces)
print(length_of_fullname)

