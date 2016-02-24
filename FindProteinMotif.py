import urllib
import re
str1 ="""P00749_UROK_HUMAN
Q8LCP6
Q7TMB8
A5GVY9
P06870_KLK1_HUMAN
P07204_TRBM_HUMAN
Q58CQ5
Q8WW18
Q9QSP4
P11279_LMP1_HUMAN
Q83I57
C0Q5J8
P07725_CD8A_RAT
P01189_COLI_HUMAN"""

url = "http://www.uniprot.org/uniprot/"
nglyc = "(?=N[^P][ST][^P])"

data = str1.split("\n") 
for prot in data:
	f = urllib.urlopen(url+prot+".fasta")
	text = f.read()
	strs = text.split("\n")
	text = ''.join(strs[1:])
	# print(text)
	pos = [m.start()+1 for m in re.finditer(nglyc, text)]
	if len(pos) > 0:
		print(prot)
		print(' '.join(map(str,pos)))
	# print(text)
