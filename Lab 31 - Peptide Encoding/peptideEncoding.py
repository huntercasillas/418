# Hunter Casillas

codons = {
    'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T',
    'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 'AGA': 'R', 'AGC': 'S',
    'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I', 'AUG': 'M',
    'AUU': 'I', 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 'CGA': 'R',
    'CGC': 'R', 'CGG': 'R', 'CGU': 'R', 'CUA': 'L', 'CUC': 'L',
    'CUG': 'L', 'CUU': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E',
    'GAU': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'GUA': 'V',
    'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 'UAA': '*', 'UAC': 'Y',
    'UAG': '*', 'UAU': 'Y', 'UCA': 'S', 'UCC': 'S', 'UCG': 'S',
    'UCU': 'S', 'UGA': '*', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C',
    'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F',
}

def reverse_complement(sequence):
    complement = list(sequence)
    for index, i in enumerate(complement):
        if i == 'A':
            complement[index] = 'T'
        elif i == 'T':
            complement[index] = 'A'
        elif i == 'C':
            complement[index] = 'G'
        elif i == 'G':
            complement[index] = 'C'

    reverse = "".join(complement)
    return reverse[::-1]

def rna_codon(dna):
    codon = ''
    i = 0
    while i < len(dna):
        key = dna[i:(i + 3)]
        if key in codons:
            codon += codons[key]
        else :
            codon += ' '
        i += 3
    return codon


def peptide_encoding(dna, codon):
    reversed_rna = reverse_complement(dna).replace('T', 'U')
    rna = dna.replace('T', 'U')
    length = 3 * len(codon)
    peptides = []
    n = len(dna) - length

    for i in range(n):
        code = dna[i:(i + length)]
        peptide = rna[i:(i + length)]
        reversed_peptide = reversed_rna[(n - i):(n - i + length)]

        if rna_codon(peptide) == codon:
            peptides.append(code)
        elif rna_codon(reversed_peptide) == codon:
            peptides.append(code)

    return peptides

def get_input(filename):
    file = open(filename, 'r')
    data = file.read().strip().split()
    dna, peptide = data[0], data[1]
    return dna, peptide


dna, peptide = get_input("rosalind_ba4b.txt")
answer = peptide_encoding(dna, peptide)
print("\n".join(answer))
