# Accept four distinct integers as input from the user. Print in ascending order if the four numbers have been entered in ascending order, and print not in ascending order otherwise.


# Accept four distinct integers in one line
a, b, c, d = map(int, input("Enter four distinct integers separated by space: ").split())

# Check if they are in ascending order
if a < b < c < d:
    print("Ascending order")
else:
    print("Not in ascending order")


#solution
#Enter four distinct integers separated by space: 2 3 5 6
#Ascending order


#Enter four distinct integers separated by space: 6 5 4 1
#Not in ascending order
