# Printing addition of integers
a = 10
b = 20
print(a+b)

# Type operator
c = 34
d = "Hello"
print(type(c))
print(type(d))

# Positive/Negative check
A = int(input("Enter first no.:\n"))
B = int(input("Enter second no.:"))
for i in (A, B):
    if i > 0:
        print(i, "is Positive")
    elif i == 0:
        print("")
    else:
        print(i, "is Negative")

# Sum of square of odd nos
sqr = 0
for i in range(a, b):
    if i % 2 != 0:
        sqr = sqr + (i * i)
print("Sum of square of odd nos between a to b is: ", sqr)
