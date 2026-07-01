# 2) generate the below pattern
#     ```
#         *
#        **
#       ***
#      ****
#     *****
#     ```

# print("    *")
#print("   **")

# solution
rows = 2

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * i
    print(spaces + stars)