# Write a code to accept a string as input and determine if it is a palindrome or not.

s = input("Enter the string: ")
rev=""

for i in s:    #sant
    rev = i+rev #tnas
    
if s == rev:
    print("palindrome")

else:
    print("Not palindrome ")
 
 #solution
""" Enter the string: madam
palindrome"""