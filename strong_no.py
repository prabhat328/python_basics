# st = "Hello World"
# print((st + " ") * 2)
# print(st * 2)


# pack = "prabhat", "anand", "tiwari", "fy bscit", "079"
# (first, middle, last, *detail) = pack
# print(detail)
# print(detail[0])
# print(pack[2])
# print(type(pack))

num = int(input("Enter a no to check if it is a strong no.:\n"))
og_num = num
fact = 0
def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n-1))

while(num >0):
    fact = fact + factorial(num%10)
    num = int(num/10)

if(fact == og_num):
    print("Given no. is a strong no.")
else:
    print("Given no. is not a strong no.")