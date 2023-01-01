# Prac 1
# QA
a = 10
b = 20
print(a+b)

# QB
c = 34
d = "Hello"
print(type(c))
print(type(d))

# QC
A = int(input("Enter first no.:\n"))
B = int(input("Enter second no.:"))
for i in (A, B):
    if i > 0:
        print(i, "is Positive")
    elif i == 0:
        print("")
    else:
        print(i, "is Negative")

# QD
sqr = 0
for i in range(10, 51):
    if i % 2 != 0:
        sqr = sqr + (i * i)
print("Sum of square of odd nos between 10 to 50 is: ", sqr)