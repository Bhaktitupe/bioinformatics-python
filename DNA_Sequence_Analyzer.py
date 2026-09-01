from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

fasta_files =""">Gene1_Human
ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG

>Gene2_Mouse
ATGCGTATCGGCTAGCTAGCTAGCGTAGCTAGCTAA

>Gene3_Bacteria
ATGAAACCCGGGTTTAAACCCGGGATGCGCTAA

>Gene4_Plant
ATGGGTTTCCCAAAGGGTTTCCCAAATAG

>Gene5_Virus
ATGCTGCTGCTGATCGATCGATCGTAA
"""
with open("sample.fasta", "w") as f:
    f.write(fasta_files)
    print("file created")    
longest_sequence = None
shortest_sequence = None
highest_gc = 0
lowest_gc = 100
sum_gc = 0
count = 0
records = []
total_sequences = 0
translation = []


# Read FASTA file and analyze sequences
for record in SeqIO.parse("sample.fasta","fasta"):
    print(record.id)
    print(record.description)
    print(record.seq)
    print(len(record.seq))
    print("-"*60)


 # Calculate GC and AT content   
    seq = str(record.seq)
    g = seq.count("G")
    c = seq.count("C")
    a = seq.count("A")
    t = seq.count("T")
    total_gc = ((g+c)/len(record.seq))*100
    total_at = ((a+t)/len(record.seq))*100
    print("gc content: ", total_gc, "%")
    print("at content: ", total_at, "%")
    print("-"*60)


 # Find longest and shortest sequences   
    total_sequences += 1
    if longest_sequence is None or len(record.seq) > len(longest_sequence):
        longest_sequence = record.seq
    if shortest_sequence is None or len(record.seq) < len(shortest_sequence):
        shortest_sequence = record.seq


# Generate reverse complements        
    reverse_record = record[:]
    reverse_record.seq = record.seq.reverse_complement()
    records.append(reverse_record)    


# Generate translations    
    translation_record = record[:]
    translation_record.seq = record.seq.translate()
    translation.append(translation_record)


# Calculate GC statistics    
    if total_gc > highest_gc:  
        highest_gc = total_gc
    if total_gc <  lowest_gc:
        lowest_gc = total_gc 
    sum_gc += total_gc
    count += 1
average_gc = sum_gc / count  

     
# Save output FASTA files    
SeqIO.write(records,"reverse_complement.fasta", "fasta") 
print("Reverse complement file created")
SeqIO.write(translation,"translation.fasta", "fasta") 
print("Translation file created")
print("Longest sequence: ",longest_sequence)
print("Shortest sequence: ", shortest_sequence)
print("Highest GC content: ", highest_gc)
print("Lowest GC content: ",lowest_gc)
print("Total sequence: ",total_sequences)
print("Average GC content: ", average_gc)

