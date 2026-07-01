# 1) generate the following pattern using print statements
#     ```
#       *
#      **
#     ***
#     ****
#     *******
#     *********#
#     i don't know what to type
#     ```

#print("    *")
#print("   **")
#print("  ***")
#print(" ****")
#print("*******")
#print("*********")

# solution
rows =10

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * i
    print(spaces + stars)