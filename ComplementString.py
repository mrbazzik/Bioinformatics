dict={"A":"T","T":"A","C":"G","G":"C"}
str="TCGGTCCGTCGGCCCGAATGCGGTCTGCCCAGTTCGCGATAACTCACCCATAGGATACGGATGCTGGGTCATTGGCTTACCTAGTCCGTTTAGGTTAACCCCGCCTAGACCCGGATGGGAAGAAATTCCTGGCTAATCTCACCCCGCCGCTTGCGCTCAACCCTGTGGTGAGCCTACGACGCCTAGGGGGGTATTTAGACGCCGAGAACTTGTAATGGCACCGCAGGGGTAGAATTAGCAAGAACAGTTTTATACTAACCCCTCAGATGCGAGTCCCAATTAAAACAAGTCGCGAGACACCGGGCTATCCTGTGCGCCCTCGCCCGACGCAAACATTAGCAGACTACTTGCGGTTATTATCAATGACAATTCGGAAACTGGTCGGCGCAATTAATTTTCAGGGGTGTCGTGTCGAGGACTGTCCGAGTCCGAATGTCATTCATAATCTGCTTAGTTGCTGCCTGTGCGGGCCGTCGACACACCACTGAAGGCAACCGAGTAACTAAATCGTATGAGCAGTGTGCTCGACTCTGTGAACGGATTAACCGAGTCGGATTTCACCTCTACAAGAGATCGGCAGGCTGCCTGGGTCTGATGATAGAGTCCCCTCTAGCCTTCTGCGAAGCACAATTACGAGTGCATCCTGTCTTCAGTTAGGCTCTCAATCATTGACTCGTTACAGGATTGGAATCCTGGGGTTCTCTGGGTGGACTCCTTAGCCGATATCTGCACTTGGCCCGCGAGCCACTTCACTAGGGATCCCGCGCCATCTTTTTGATTAGTCGACTTATGAAGGGCCCGTTATACGTCAGCACGGT"
str1=str[::-1]
res=[dict[k] for k in str1]
print(''.join(res))