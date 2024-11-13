

# 📖Python Conditional Statements:


### 1. The if Statement
The if statement is used to test a condition. If the condition is True, the block of code inside the if statement is executed.
  ###### Syntax:
            if condition:
            
               # Code to execute if the condition is True
#####   Example:
      x = 10
      if x > 5:
          print("x is greater than 5")    

          #output gives x is greater than 5

### 2. The else Statement
The else statement provides an alternative block of code that executes if the condition in the if statement is False.
 ###### Syntax:
          if condition:
             # Code to execute if the condition is True
          else:
             # Code to execute if the condition is False
 ##### Example:
         x = 3
         if x > 5:
             print("x is greater than 5")
         else:
             print("x is not greater than 5")

            #Output gives:
            
               x is not greater than 5

 ### 3.  The elif Statement
The elif (short for "else if") statement allows you to check multiple conditions. If the first condition is False, it checks the next elif condition.
  ###### Syntax:
           if condition1:
               # Code to execute if condition1 is True
           elif condition2:
               # Code to execute if condition2 is True
           else:
               # Code to execute if all above conditions are False

 ##### Example:
          x = 10
          if x > 15:
             print("x is greater than 15")
          elif x == 10:
             print("x is exactly 10")
          else:
             print("x is less than 10")


            # Output gives:

               x is exactly 10



### 🛑Perform a python program to check whether the input year is Leap year or not.

###### 📟Sample Output:
          Enter the Year:2024
          
          2024 is a leap year!
               
               


            



             





