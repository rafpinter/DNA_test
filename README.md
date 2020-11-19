# DNA_test
DNA test to identify sample DNA from a people database


**USAGE**

"python dna.py data.csv sequence.txt"


**DATABASE FILE**
You must have a database on a csv file containing the name of the person and the repetition number of the respective STR region:

Name, STR1, STR2, STR3,...

Example:
name,AGATC,TTTTTTCT,AATG,TCTAG,GATA,TATC,GAAA,TCTG

**DNA SAMPLE FILE**

You must have your DNA sample on a .txt file

Example:
AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG
