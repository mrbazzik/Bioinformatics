import re
dict = {"TTT": "F",      "CTT": "L",      "ATT": "I",      "GTT": "V",
"TTC": "F",      "CTC": "L",      "ATC": "I",      "GTC": "V",
"TTA": "L",      "CTA": "L",      "ATA": "I",      "GTA": "V",
"TTG": "L",      "CTG": "L",      "ATG": "M",      "GTG": "V",
"TCT": "S",      "CCT": "P",      "ACT": "T",      "GCT": "A",
"TCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
"TCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
"TCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
"TAT": "Y",      "CAT": "H",      "AAT": "N",      "GAT": "D",
"TAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
"TAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
"TAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
"TGT": "C",      "CGT": "R",      "AGT": "S",      "GGT": "G",
"TGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
"TGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
"TGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"}

str1 = """>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"""
data = str1.split("\n")[1:]
print(data)
for dat in data:
	starts = [m.start() for m in re.finditer("(?=ATG)",dat)]
	ends = [m.start() for m in re.finditer("(?=TAA|TAG|TGA)",dat)]
	print(starts)
	print(ends)
	for start in starts:
		cur_end = None
		for end in ends:
			if end > start:
				cur_end = end
				break
		# print(cur_end)
		if cur_end != None:
			text = dat[start:cur_end]
			if len(text)%3 != 0:
				continue
			print(text)
			i = 0
			out = ""
			while i < len(text):
				amino = dict[text[i:i+3]]
				if amino != "Stop":
					out += amino
				i = i+3
			print(out)
