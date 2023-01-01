factor_list = []
def factor(p):
    for i in range(1, (p+1)):
        if p%i == 0:
            print(i)
            factor_list.append(i)
            i += 1
    return(factor_list)

a = int(input('Enter an integer:\n\t'))
print(factor(a))

def addition():
    a = 10
    b = 20
    return(a + b)

print(f'addition of a and b is: {addition()}')
# print(f'Sum of {a} and {b} is {sum(a, b)}')
