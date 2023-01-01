# Practical 4

# QA
lis = [2, 3, 'a', 4, 'p']
# accessing
print(lis)
print(lis[2])
print(lis[2:4], end = '\n\n')

# traversing
for i in lis:
    print(i)

print('')

# removing
lis.pop()
print(lis)

lis.pop(1)
print(lis)

lis.remove(2)
print(lis)

del lis[0]
print(lis)


# QB
tup = (0, 7, 'p', 9, 't')
# accessing
print(tup)
print(tup[3])
print(tup[:4])

# traversing
for i in tup:
    print(i)

# removing
# tuple is immutable, hnece elements cannot be changed. A new tuple can be made using existing tuple
tup1 = tup[:2] + tup[3:]
print(tup1)

# packing
name = "Prabhat", "Anand", "Tiwari", "FY", "BSCIT"

# unpacking
(first, *middle, last) = name

print(middle)
print(name[1])