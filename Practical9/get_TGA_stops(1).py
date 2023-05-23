# Import the built-in library
import io

# Create a new fasta file to store the results
output_handle = open("TGA_genes.fa", "w")

# Read the original fasta file
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as input_handle:
 # Initialize an empty string to store the current gene record
 gene_record = ""
 # Loop through each line in the file
 for line in input_handle:
 # Check if the line starts with ">"
 if line.startswith(">"):
 # If this is not the first gene record, process it
 if gene_record:
 # Convert the string to a file-like object
 gene_file = io.StringIO(gene_record)
 # Read the gene name
 gene_name = gene_file.readline().strip().split("|")[3]
 # Read the gene sequence
 gene_seq = gene_file.read().replace("\n", "")
 # Check if the gene sequence ends with TGA
 if gene_seq.endswith("TGA"):
 # Write the gene record to the new fasta file
 output_handle.write(f">{gene_name}\n{gene_seq}\n")
 # Reset the gene record string
 gene_record = ""
 # Append the line to the gene record string
 gene_record += line
 # Process the last gene record
 if gene_record:
 # Convert the string to a file-like object
 gene_file = io.StringIO(gene_record)
 # Read the gene name
 gene_name = gene_file.readline().strip().split("|")[3]
 # Read the gene sequence
 gene_seq = gene_file.read().replace("\n", "")
 # Check if the gene sequence ends with TGA
 if gene_seq.endswith("TGA"):
 # Write the gene record to the new fasta file
 output_handle.write(f">{gene_name}\n{gene_seq}\n")

# Close the output file
output_handle.close()
