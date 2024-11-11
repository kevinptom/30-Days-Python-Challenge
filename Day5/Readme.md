# Basic String Functions in Python


 ## 1. String Length: len()
Description: Returns the number of characters in a string.
 Syntax:
  len(string)
##### Example:
        print(len("Hello"))  # Output: 5

 ## 2.    title()
Converts the first character of each word to uppercase.

Syntax: text.title()  #where text is an variable where input string is stored
##### Example:
        print("hello world".title())  # Output: Hello World

 ## 3.    replace()
Replaces all occurrences of a substring with another substring.

Syntax:    text.replace(old, new)
#####   Example:
        print("Hello, World".replace("World", "Python"))  # Output: Hello, Python

 ## 4.   split()
    Splits the string into a list based on a delimiter (default is space).   
    
    Syntax:  text.split(delimiter)
##### Example:
       print("apple,banana,cherry".split(","))  # Output: ['apple', 'banana', 'cherry']



#### 🛑Problem Statement: Write a Python program that takes a user's full name as input. The program should:

Convert the name to all uppercase letters.

Convert the name to all lowercase letters.

Capitalize the first letter of each word.

Count the total number of characters in the name (excluding spaces).


## Expected Output:  (Example)

Original Name: Amanda Smith

Uppercase: AMANDA SMITH

Lowercase: amanda smith

Title Case: Amanda Smith
 
Total Characters (excluding spaces): 11













