# Hunter Casillas 

def reverseCompliment(sequence):

    compliment = list(sequence)

    for index, i in enumerate(compliment):
        if i == 'A':
            compliment[index] = 'T'
        elif i == 'T':
            compliment[index] = 'A'
        elif i == 'C':
            compliment[index] = 'G'
        elif i == 'G':
            compliment[index] = 'C'

    reverse = "".join(compliment)
    reverse = reverse[::-1]

    print(reverse)

nucleotide = "AAAACCCGGT"

reverseCompliment(nucleotide) 
