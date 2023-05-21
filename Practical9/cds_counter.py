import math
import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
r_list = []
index=-1
while True:
        index = seq.find('AT',index+1)
        if index==-1:
            break
        r_list.append(index)`
sta = re.search('ATG',seq)
#ckeck if thedifference between ending and start is mutiple of three
end = re .findall('TRA',seq)
n = 0
a = 1
while a < math.ceil(len(seq)/3):
 if sta + 3 == end:
   n += 1
 else :
   a += 1
print (n)  
