# Hunter Casillas

def hammingDistance(p, q):
    distance = 0
    
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1

return distance


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


def motifEnumeration(dna, k, d):
    
    final = []
    
    for i in range(len(dna)):
        kmers = set()
        for j in range(len(dna[i]) - k + 1):
            pattern = dna[i][j:j + k]
            kmers.update(neighbors(pattern, d))
            kmers.add(pattern)
        final.append(kmers)
    
    patterns = final[0]

for pattern in final[1:]:
    patterns.intersection_update(pattern)
    return patterns


dna = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]
k = 3
d = 1

print(*motifEnumeration(dna, k, d))
