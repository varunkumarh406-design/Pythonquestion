# 1) What will be the output of the below code?
#
# ```python
# print("hello","world")
# ```

"""
=========================================================
💡 DETAILED SOLUTION & EXPLANATION
=========================================================

Expected Output:
----------------
hello world

Why this happens (Under the Hood):
----------------------------------
1. Multiple Arguments: The `print()` function in Python can take multiple arguments separated by commas. Here, we are passing two string arguments: "hello" and "world".
2. The `sep` Parameter: By default, the `print()` function has a hidden parameter called `sep` (separator) which is set to a single space character (`sep=" "`). 
3. Concatenation: When Python prints multiple arguments, it automatically inserts the `sep` string (the space) between each argument. 

Advanced Tip 🚀:
----------------
If you wanted to change the behavior so they print together without a space, or with a different character (like a hyphen), you would explicitly pass the `sep` parameter:
  print("hello", "world", sep="-")  # Output: hello-world
  print("hello", "world", sep="")   # Output: helloworld

=========================================================
"""

# Try it yourself!
print("hello", "world")
