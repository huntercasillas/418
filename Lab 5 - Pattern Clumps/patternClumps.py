# Hunter Casillas

from collections import defaultdict

def patternClumps(genome, k, l, t):
    
    lookup = defaultdict(list)
    answer = set()
    
    for index in range(len(genome) - k + 1):
        clump = genome[index:index + k]
        
        while lookup[clump] and index + k - lookup[clump][0] > l:
            lookup[clump].pop(0)
    
        lookup[clump].append(index)
        
        if len(lookup[clump]) == t:
            answer.add(clump)

print(answer)


genome = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
k = 5
l = 75
t = 4

patternClumps(genome, k, l, t)
