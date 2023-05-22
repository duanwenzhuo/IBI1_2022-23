import numpy as np
from Bio import SeqIO
from Bio.SubsMat import MatrixInfo



#read sequence
seq_file_1 = open('F:/IBI/Practical11/ACE2_mouse.fa', "r")
seq_file_2 = open('F:/IBI/Practical11/ACE2_cat.fa', "r")
seq_file_3 = open('F:/IBI/Practical11/ACE2_human.fa', "r")
seq_mouse = next(SeqIO.parse(seq_file_1, "fasta")).seq
seq_cat = next(SeqIO.parse(seq_file_2, "fasta")).seq
seq_human = next(SeqIO.parse(seq_file_3, "fasta")).seq
seq_file_1.close()
seq_file_2.close()
seq_file_3.close()

#define a function that compare two sequence
def global_alignment_score(seq1, seq2, matrix, gap_penalty):
    # initialize a score matrix with zeros
    m = len(seq1) + 1 # number of rows
    n = len(seq2) + 1 # number of columns
    score_matrix = np.zeros((m, n))
    
    # fill the first row and column with gap penalties
    for i in range(m):
        score_matrix[i, 0] = i * gap_penalty
    for j in range(n):
        score_matrix[0, j] = j * gap_penalty
    
    # fill the rest of the matrix with scores based on the matrix and gap penalty
    for i in range(1, m):
        for j in range(1, n):
            # get the amino acids from the sequences
            aa1 = seq1[i-1]
            aa2 = seq2[j-1]
            # get the substitution score from the matrix
            if (aa1, aa2) in matrix:
                sub_score = matrix[(aa1, aa2)]
            elif (aa2, aa1) in matrix:
                sub_score = matrix[(aa2, aa1)]
            else:
                sub_score = 0 # default score for unknown amino acids
            # calculate the scores for match/mismatch, insertion and deletion
            match_score = score_matrix[i-1, j-1] + sub_score
            insert_score = score_matrix[i-1, j] + gap_penalty
            delete_score = score_matrix[i, j-1] + gap_penalty
            # choose the maximum score and store it in the matrix
            score_matrix[i, j] = max(match_score, insert_score, delete_score)
    
    # return the bottom-right corner of the matrix as the final score
    return score_matrix[m-1, n-1]
def compare (seq1,seq2):   
    for line in seq1 and seq2:
        if line[0] != '>':
            edit_distance = 0
            for i in range(len(seq1) - 1) and range(len(seq2) - 1):
                if seq1[i] != seq2[i]:
                    edit_distance += 1
    return edit_distance






# calculate the global alignment score using global_alignment_score()
score1 = global_alignment_score(seq_mouse,seq_cat, MatrixInfo.blosum62, -5)
score2 = global_alignment_score(seq_mouse,seq_human, MatrixInfo.blosum62, -5)
score3 = global_alignment_score(seq_cat,seq_human, MatrixInfo.blosum62, -5)

print('the alignment score for mouse and cat is:',score1)
print('the alignment score for mouse and human is:',score2)
print('the alignment score for human and cat is:',score3)

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
