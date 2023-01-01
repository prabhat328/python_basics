# Q2)
def h(n):
    s = 0
    for i in range(2,n):
        if n%i == 0:
           s = s+i
           print(s)
    return(s)


# Q3)
def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m/n)
        print(res)
    return(res)

h(60)

g(375,4)

print("Hii")
