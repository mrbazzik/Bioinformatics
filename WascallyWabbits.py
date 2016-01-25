fs = [1,1]

def Fib(n):
 	for i in range(2,n):
 		fs.append(fs[i-2]+fs[i-1])
 	return fs[n-1]


def Rab(n, k):
	rs = [1,1]
 	for i in range(2,n):
 		rs.append(rs[i-1]+k*rs[i-2])
 	return rs[n-1]
print(Rab(28,4))