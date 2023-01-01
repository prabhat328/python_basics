# method 1
name = 'prabhat'
i = 0
while i <= (len(name) - 1):
    print(name[i])
    i += 1

print(name)

# method 2
string = 'prabhat'
a = 0
while a <= len(string): # here, <= is used beacuse slicing used below does not include last index value
    newstr = string[a: a+1]
    print(newstr)
    a += 1
    print(a)

print(string[0: ])