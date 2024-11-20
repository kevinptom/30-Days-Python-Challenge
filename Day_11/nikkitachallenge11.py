author:Nikkita
created on:20/11/24
program to print factorial of a number using while loop

num=int(input("Enter your number:"))
factorial=1
store_num=num
while num>0:
    factorial=factorial*num
    num=num-1
print("The factorial of ",store_num," is :",factorial)
