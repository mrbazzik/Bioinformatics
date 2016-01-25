from math import factorial 
def NumAaBb(k, n):
	sum = 0
	total = pow(2,k)
	for i in range(n,total+1):
		print(i)
		sum += float(factorial(i))/factorial(total-i)*pow(float(1)/4,i)*pow(float(3)/4,total-i)
	return sum
print(NumAaBb(2,1))
