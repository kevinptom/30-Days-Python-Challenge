'''
author: pace petson
created on 13/1/24
program to print users full name as in put
version1.0
'''
name=input("orginal name:")
print("uppercase:",name.upper())
print(f"lowercase:{name.lower()}")
print("title case:",name.title())
name_space=name.replace(" "," ")
print("total characters excluding spaces:",len(name_space))