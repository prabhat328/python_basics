# to swap numbers
def swapnum(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

def fibonacc(a, b):
    # if passed parameters are not in required order
    if(a>b):
        proper_input = swapnum(a,b)
        a = proper_input[0]
        b = proper_input[1]

    print(a, end = ', ')
    # if(b > 90):
    #     return
    swapped = swapnum(a, b)
    a = swapped[0]
    b = swapped[1]
    b = a + b
    
    return fibonacc(a, b)

fibonacc(0,1)