def is_protein(sequence):
    import re
    seq = sequence.upper()
    c = 'ATG([AGCT]{3})*TGA'
    if len(re.findall(c, seq)) > len(seq)*50//100:
        print('protein-coding')
    elif len(re.findall(c, seq)) < len(seq)*10//100:
        print('nonprotein-coding')
    else:
        print('unclear')


#example
is_protein('AAGCTGTCAGTGCTAGCTGTCAGTGCTAGTGCGAGCGTAGTGATGTGTCGTAGTCGTGCGTAGTG')
        

