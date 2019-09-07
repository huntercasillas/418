# Hunter Casillas

def nucleotideCount(sequence):
    a = sequence.count('A')
    c = sequence.count('C')
    g = sequence.count('G')
    t = sequence.count('T')
    print(a, " ", c, " ", g, " ", t)

testNucleotide = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

sequenceCount(testNucleotide) 
