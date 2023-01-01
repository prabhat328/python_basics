import math
def fact(num):
    abc = 1
    for i in range(1,num +1):
        abc = abc * i
    return abc



def estimate_pi():
    sum = 0
    k = 0
    while True:
        numerator = (fact(4*k))*(1103 + (26390*k))
        denominator = (fact(k)**4)*(396**(4*k))
        sum = sum + (numerator/denominator)
        k = k + 1
        if abs(sum) < 1e-15:
            break
        print(sum)
    rhs = ((2*sqrt(2))/9801) * sum
    return 1/rhs

print(estimate_pi())