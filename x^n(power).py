def power(base, power):
    number = 1
    for i in range(1, (power + 1)):
        number = number * base
        # print(number)
    return number 

# power(10,5)
print(power(10, 5))
