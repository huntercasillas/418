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


pattern = "ACG"
d = 1

print(*neighbors(pattern, d))
