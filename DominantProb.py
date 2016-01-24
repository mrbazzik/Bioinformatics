def ProbDomin(k,m,n):
	total = k+m+n
	return 1-float(m)/total*float(m-1)/(total-1)*0.25-float(m)/total*float(n)/(total-1)*0.5-float(n)/total*float(n-1)/(total-1)-float(n)/total*float(m)/(total-1)*0.5

print(ProbDomin(16,23,26))
