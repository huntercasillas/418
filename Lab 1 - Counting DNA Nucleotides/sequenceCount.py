# Hunter Casillas

def sequenceCount(sequence):
    a = sequence.count('A')
    c = sequence.count('C')
    g = sequence.count('G')
    t = sequence.count('T')
    print(a, " ", c, " ", g, " ", t)

testSequence = "GGGTCAGACCGTCAGGAGCTCACGGGTCAACGTGTTCACGCAACCAACCTGCTGTCCGGCGACATTACCGTTCCCAACCACCTCACCCCCTGCCGGCTCACTGCTGAGACCCAGCACAACCTCCTTTTAATTGCCAGCGGGAGCTCCCTTTTCGCTCCTCGCCATTTGTCACTCAAACACTCCACCGAAGGCGAGCTGCGATAGGCTCGCCAACGGGGTCGGGCGGTTTTGCTACTCAACGGTCTCGGAGTACGCCGCGGCGCCGCTAACGCGAAGGACGTGCCTGAGGCCGTTTTGCTGGTAGCAACAGTTTTTAGAGGCTATTCTAAGCGCTGGCTGCCTGTTGGCAGCTTCGTGTATCCTATGAGTTAGGCATGCGCGGTAGGGCTTATGCAGTAATCTAAGTACCTCAGTGGTCCCCGCGTAGCCATAGCAGGCGAGCTGCAAGCCCCTCGGCCCTGTTTTTGGAGAGCGAGAATTCTGTGGCACATGTGGCCGACGCAAGAGAGGGACGCTCCTAGCAGGAGTAGCCGTCTCAATAGGGTTGGACTAAGCAATCCTTACCTCGTGCGACGGAAAAGTTTTCGTACGCCACGGCCAATGACTGCGGCTGTTAGTAATGCCTATCCGGATCTATATGATCCGCAACATTTAGGCCCTCGGGGAGTATACCATATTGTCGAATGTTAGCGGGTCTCGTAGACGCCGTCTTTTACGCGAGTAATGCTATGTGCGTACGCGGGCAGCAATTTAGATATATGGACCGCATAGTGATATGCATAAGGCAATCTCCGCCACCCCCGAATTCCGTGGAGGGCGATCAGATGCGATGGCTAACGGTGTG"

sequenceCount(testSequence)
