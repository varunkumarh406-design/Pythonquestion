# Write a program to accept the positive integer n from the user and print the cube of all
# numbers from 1 to n.

n=int(input("Enter the number : "))

for i in range(1,n+1):
     cube=i**3
     print(f"Current number is :{i} and the cube is {cube}")


#solution
"""Enter the number : 4
Current number is :1 and the cube is 1
Current number is :2 and the cube is 8
Current number is :3 and the cube is 27
Current number is :4 and the cube is 64"""