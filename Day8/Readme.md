# 📖Basics of Logical Operators in Python

Logical operators in Python are used to perform logical operations on boolean values (`True` and `False`). These operators are often used in conditional statements and loops to control the flow of a program. Python provides three main logical operators:

- `and`
- `or`
- `not`

## 1. `and` Operator

The `and` operator returns `True` only if **both** conditions are `True`. If either of the conditions is `False`, the result is `False`.

### Syntax
    ```python
     condition1 and condition2

#### Example:
      a = 5
      b = 10
      if a < b and b < 15:
           print("Both conditions are True")
      else:
           print("At least one condition is False")

    #output :
       Both conditions are True


## 2. 'or' Operator

  The or operator returns True if at least one of the conditions is True. If both conditions are False, the result is False.

### Syntax
   condition1 or condition2
#### Example:
       a = 5
       b = 20
       if a > 0 or b < 15:
           print("At least one condition is True")
       else:
           print("Both conditions are False")

       #Output :
           At least one condition is True


## 3. 'not' Operator
  The not operator is used to invert the value of a boolean. It converts True to False and False to True.

### Syntax
  not condition
#### Example:
   a = True
   print(not a)  # Outputs: False

   b = False
   print(not b)  # Outputs: True


## 4.  Combining Logical Operators
You can combine multiple logical operators in a single expression. Python evaluates these expressions from left to right, but you can use parentheses to control the order of evaluation.

#### Example:
     a = 5
     b = 10
     c = 15

    #Using `and`, `or`, and `not` together
    
     if (a < b and b < c) or not (c == 15):
            print("Condition is True")
     else:
            print("Condition is False")

#Output gives:
   Condition is True



## 🛑Perform a python program to find the smallest of three numbers.


##### 📟Expected Output:
   Enter the first number: 8
   
   Enter the second number: 3
   
   Enter the third number: 5
   
   The smallest number is: 3

   

           


      

