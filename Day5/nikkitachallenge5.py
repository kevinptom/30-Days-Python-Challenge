""""
author:Nikkita Anna George
created on:12/11/24
program to print user's full name as input
version 1.0
"""
name=input("Original name:")
print("uppercase:",name.upper())
print(f"lowercase:{name.lower()}")
print("title case:",name.title())
name_space=name.replace(" ","")
print("Total characters excluding spaces:",len (name_space))
