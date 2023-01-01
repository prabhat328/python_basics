# Pract 2

# QA
a = 5.76345
b = 30
# 1
ma = max(a, b)
print(ma)
# 2
mi = min(a, b)
print(mi)
# 3
ty = type(a)
print(ty)
# 4
init = int(a)
print(init)
# 5
ran = range(a,b)
print(ran)

# QB
def vol_sphere(r):
    volume = (4/3) * 3.14 * (r ** 3)
    print(volume)


radius = int(input("Enter radius of sphere to get it`s volume\n"))
vol_sphere(radius)

# QC
def factorial(a):
    if a == 0 or a ==1:
        return 1
    else:
        return (a * factorial(a - 1))


print(factorial(10))