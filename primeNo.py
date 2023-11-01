#******************   PRIME NUMBERS   ******************

#using normal range(full range)(0(n))
n = input("Enter a number to check if it is prime\n")
try:
	int(n)
except:
	print('Please enter a numeric value\n')

else:
	check = 0
	p = int(n)
	for i in range(2,p):
		if p%i==0:
			break;
		check+=1;

	if (check == (p-2)):
		print(p)

#using half range(0(n/2))
for n in range(2,100):
	check = 0
	for i in range(2,n//2 + 1):
		if n%i==0:
			break;
		check+=1

	if (check == ((n//2 + 1) - 2)):
		print(n, end = ',')
print()

#using square root range(0(n^0.5))
for n in range(2,100):
	check = 0
	for i in range(2,int(n**0.5) + 1):
		if n%i==0:
			break;
		check+=1

	if (check == (int(n**0.5) + 1 - 2)):
		print(n, end = ',')
print()

#using 6n+1,6n-1(0(1))(fastest)
n = int(input('Enter an integer:\n'))
if n<=1:
	print(f'{n} is not a prime no.')
elif(n==2 or n==3):
	print(f'{n} is a prime no.')
else:
	if((n-1)%6 == 0 or (n+1)%6 == 0):
		print(f'{n} is a prime no.')
