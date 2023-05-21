# Initialize score matrix
score_matrix =[]
for i in range(len(seq1)):
    row=[]
    for j in range(len(seq2)):
        row.append(blosum.get((seql[i]，seq2[j])，-4))
    score_matrix.append(row)