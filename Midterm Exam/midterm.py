# Hunter Casillas

def hammingDistance(p, q):
    distance = 0

    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1

    return distance


def reverseCompliment(sequence):

    compliment = list(sequence)

    for index, i in enumerate(compliment):
        if i == 'a':
            compliment[index] = 't'
        elif i == 't':
            compliment[index] = 'a'
        elif i == 'c':
            compliment[index] = 'g'
        elif i == 'g':
            compliment[index] = 'c'

    reverse = "".join(compliment)
    reverse = reverse[::-1]

    return reverse


def neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']

    neighborhood = set()
    suffixNeighbors = neighbors(pattern[1:], d)


    for text in suffixNeighbors:
        if hammingDistance(pattern[1:], text) < d:
            for nucleotide in "ACGT":
                neighborhood.add(nucleotide + text)
            else:
                neighborhood.add(pattern[0] + text)

    return neighborhood


# REVERSE COMPLIMENT
nucleotide = "acatttgacttcc"
print(reverseCompliment(nucleotide))

# HAMMING DISTANCE
p = "ACTAAGACTCAGGG"
q = "ATGCCGACTCGAGG"
print(hammingDistance(p, q))

# NEIGHBORHOOD
pattern = "CTAGACCTAG"
d = 3
print(*neighbors(pattern, d))
