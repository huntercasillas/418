# Hunter Casillas

codons = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}

def translate_protein(rna):
    protein = ''
    i = 0
    while i < len(rna):
        n = codons[rna[i:i+3]]
        if n == 'Stop':
            break
        protein += n
        i += 3
    return protein

def get_input(filename):
    file = open(filename, 'r')
    data = file.read().strip().split()
    return data[0]


rna = get_input("rosalind_ba4a.txt")
answer = translate_protein(rna)
print(answer)
