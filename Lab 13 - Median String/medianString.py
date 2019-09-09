# Hunter Casillas

import math

def numberToSymbol(number):
    if number == 0:
        return 'A'
    elif number == 1:
        return 'C'
    elif number == 2:
        return 'G'
    elif number == 3:
        return 'T'
    else:
        return None


def numberToPattern(index, k):
    if k == 1:
        return numberToSymbol(index)
    
    quotient, remainder = divmod(index, 4)
    prefixPattern = numberToPattern(quotient, k - 1)
    symbol = numberToSymbol(remainder)
    return prefixPattern + symbol


def hammingDistance(p, q):
    distance = 0
    
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1

return distance

def patternDistance(pattern, dna, k):
    
    k = len(pattern)
    distance = 0
    
    for genome in dna:
        minimum = math.inf
        for i in range(len(genome) - k + 1):
            dist = hammingDistance(genome[i:i+k], pattern)
            if dist < minimum:
                minimum = dist
        distance += minimum
    
    return distance


def medianString(dna, k):
    
    distance = math.inf
    median = ""
    
    for i in range(4**k):
        pattern = numberToPattern(i, k)
        updatedDistance = patternDistance(pattern, dna, k)
        if distance > updatedDistance:
            distance = updatedDistance
            median = pattern
    return median


dna = ["GAACACTGTACGGCCTACTCCAGTTGAGATCCTAAAGTAGTG", "CATCTTTGATTGGCCTACTTGTGAAATTGAATCCGTTGATAG",
       "TGGCTGAGCAATAACTGAGTGATCTACTTTAAACGACCCTAC", "AGGGACCCTCCCTGAGTTCTCATACCAATTGCCTACCATTCT",
       "AAGCAGACCTACTGTGCACACGAGGCGGCCAACATAGGAGAC", "TCTTTGGGAGTCGTCACTGCCTACCCGTCAGACTACCTCTGG",
       "TCCTACGATACGGACCTGCTGAGATAAGATCTCTTGCTAAGT", "GCCGTCGGGCGTCCGAACTAATAAGCGGGGCCCTACCCCCAA",
       "TAGGTCTTGGACCAACTGCCCTACCCAAGCCGATGCAGTCGC", "ATGATAACCTACGACTCCGGCATGTGTAATCAGAAGGTCTAG"]
k = 6

print(medianString(dna, k))
