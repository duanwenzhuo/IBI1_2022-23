import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
s = r'ATG(?:...)*?(?:TAA|TGA)'
n = re.findall(s,seq)
print(n)
print (len(n)) 
