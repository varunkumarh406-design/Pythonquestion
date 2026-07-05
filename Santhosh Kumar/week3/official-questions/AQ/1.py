# Write a code using a while loop that adds all odd numbers from 1 to 100 (inclusive).


n=1

while n<=100:
    print(n)
    n+=2

#Using for loop

for i in range(1,101,2):
    print(i)


"""#solution
n = 1
total = 0

while n <= 100:
    print(n)
    total += n
    n += 2

print("Sum =", total)"""