# Define a function to parse a fasta file, return a generator that yields a tuple of header and sequence each time
def parse_fasta(filename):
    # Open the file
    with open(filename) as f:
        # Initialize header and sequence as empty
        header = ""
        seq = ""
        # Loop through each line
        for line in f:
            # Strip the newline character
            line = line.strip()
            # If it is a header line, split it and get the gene name
            if line.startswith(">"):
                # If there is already a header and sequence, yield them
                if header and seq:
                    yield header, seq
                # Update header as gene name
                header = line.split("|")[3]
                # Clear sequence
                seq = ""
            # If it is not a header line, update sequence
            else:
                seq += line
        # Finally if there is still a header and sequence, yield them
        if header and seq:
            yield header, seq

# Create an empty dictionary to store gene sequences and counts for different stop codons
stop_codons = {}

# Read the fasta file
for gene_name, gene_seq in parse_fasta("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"):
    # Get the last three bases of the gene sequence, which is the stop codon
    stop_codon = gene_seq[-3:]
    # Check if the stop codon is already in the dictionary, if not, create an empty list
    if stop_codon not in stop_codons:
        stop_codons[stop_codon] = []
    # Add the gene name and sequence to the corresponding stop codon list
    stop_codons[stop_codon].append((gene_name, gene_seq))

# Ask the user to input a stop codon
user_input = input("Please enter a stop codon (TAA, TAG or TGA):")

# Check if the user input is valid
if user_input in stop_codons:
    # Create a new fasta file name based on user input
    output_file = user_input + "_stop_genes.fa"
    # Open the new fasta file
    output_handle = open(output_file, "w")
    # Get the corresponding gene sequences and counts
    gene_list = stop_codons[user_input]
    gene_count = len(gene_list)
    # Loop through the gene list, write to the new fasta file, and print out the gene name and coding sequence count
    for gene_name, gene_seq in gene_list:
        output_handle.write(">" + gene_name + "\n")
        output_handle.write(gene_seq + "\n")
        print(gene_name, len(gene_seq))
    # Close the output file
    output_handle.close()
    # Print out the total gene count
    print("There are {} gene sequences that end with {}".format(gene_count, user_input))
else:
    # If the user input is invalid, print out an error message
    print("Invalid stop codon, please enter again")
