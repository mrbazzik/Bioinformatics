from math import factorial
n = 7

def makeCombs(start, rest_arr):
	if len(rest_arr) == 1:
		print(start[1:]+" " + str(rest_arr[0]))
	else:
		for i in rest_arr:
			new_start = start + " " + str(i)
			new_rest = list(rest_arr)
			new_rest.remove(i)
			makeCombs(new_start, new_rest)

print(factorial(n))
makeCombs("", range(1,n+1))
