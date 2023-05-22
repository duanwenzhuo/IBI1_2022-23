import re
def is_protein(sequence):
    
     """Determine whether a DNA sequence is protein-coding or not.

  Args:
    sequence (str): A DNA sequence.

  Returns:
    tuple: A pair of (percentage, label), where percentage is the percentage of the sequence that is coding and label is one of "protein-coding", "non-coding", or "unclear".
  """
     # Converts the DNA sequence to uppercase letters
     seq = sequence.upper()
     if re.search(r'[^ATCG]',seq):
        print ('sequence must be a valid DNA sequence')
     else:
        #Define a regular expression that matches the region between the start codon ATG and the stop codon TGA
        c = 'ATG([AGCT]{3})*TGA'
        coding_length = sum(len(match) for match in re.findall(c, seq))
        coding_percentage = coding_length / len(seq) * 100
        if coding_percentage > 50:
            label = "protein-coding"
        elif coding_percentage < 10:
            label = "non-coding"
        else:
            label = "unclear"
        return coding_percentage, label

#example
result = is_protein('AAGCTGTCAGTGCTAGCTGTCAGTGCTAGTGCGAGCGTAGTGATGTGTCGTAGTCGTGCGTAGTG')
print(result)        

