rabs = [1,1]
borns = [1,0]
deaths = [0,0]
def Rab(n,m):
	for i in range(2,n):
		if i>=m:
			dies = borns[i-m]
		else:
			dies = 0
		deaths.append(dies)
		borns.append(rabs[i-2]-deaths[i-1])
		rabs.append(rabs[i-1]+rabs[i-2]-deaths[i-1]-dies)
	return rabs[n-1]
print(Rab(87,19))