Bioinformatics with Python

This repository contains Python-based work focused on biological sequence analysis using Biopython. It documents my practical learning and application of Python programming concepts in bioinformatics.

DNA Sequence Analyzer

The dna_sequence_analyzer.py program reads DNA sequences in FASTA format and performs several basic sequence analysis tasks. It extracts sequence information, calculates sequence length, GC content, and AT content, and identifies the longest and shortest sequences.

The program also performs biological sequence transformations, including reverse complement and translation, and generates separate FASTA files containing the processed sequences. In addition, it calculates the highest, lowest, and average GC content across the input sequences.

Tools used: Python, Biopython, FASTA, and SeqIO.

This project is part of my ongoing development in Python and bioinformatics and will be expanded with additional sequence-analysis projects and workflows.

Results

The DNA sequence analyzer was tested on five sample DNA sequences. The analysis identified a longest sequence of 39 bp and a shortest sequence of 27 bp. The highest GC content was 56.41%, the lowest was 44.83%, and the average GC content across all five sequences was 50.18%. The program also successfully generated reverse-complement and translated FASTA files.


