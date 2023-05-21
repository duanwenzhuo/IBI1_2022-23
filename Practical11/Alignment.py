#read sequence
seq_mouse = open('F:/IBI/Practical11/ACE2_mouse.fa').read()
seq_cat =  open('F:/IBI/Practical11/ACE2_cat.fa').read()
seq_human =  open('F:/IBI/Practical11/ACE2_human.fa').read()


#define a function that compare two sequence
def compare(a,b):
    for line in a and b:
        if line[0] != '>':
            edit_distance = 0
            for i in range(len(a) - 1) and range(len(b) - 1):
                if a[i] != b[i]:
                    edit_distance += 1
    return edit_distance



#workflow 	for	comparing	two	sequences   
#1.Read the BLOSUM62 matrix.
#2.Compare each amino acid in Seq1 with its corresponding amino acid in Seq2.
#3.For each pair of aligned amino acids, find its score in the BLOSUM62 matrix and add it to a new vector.
#4.Sum all scores in the vector.
#5.Print Seq1 name/sequence.
#6.Optional: Print alignment.
#7.Print Seq2 name/sequence.
#8.Print scores.



d = compare(seq_mouse,seq_cat)
e = compare(seq_mouse,seq_human)
f = compare(seq_cat,seq_human)
print('the percentage of identical amino acids for mouse and cat is:',d/len(seq_cat))
print('the percentage of identical amino acids for mouse and human is:',e/len(seq_cat))
print('the percentage of identical amino acids for human and cat is:',f/len(seq_cat))
if d > e and d > f:
    print('the sequences of mouse and cat are most closely')
elif e>d and e>f:
    print('the sequences of mouse and human are most closely')
elif f>d and f>e:
    print('the sequences of cat and human are most closely')
   