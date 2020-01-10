# Hunter Casillas 

def hammingDistance(p, q):

    distance = 0
    pList = list(p)
    qList = list(q)

    for i in range(len(pList)):
        if pList[i] != qList[i]:
            distance += 1

return distance

def patternMatching(pattern, genome, mismatches):

    answer = []

    for i in range(len(genome) - len(pattern)):
        if hammingDistance(genome[i:i+len(pattern)], pattern) <= mismatches:
            answer.append(str(i))

print(*answer)


pattern = "ATTCTGGA"
genome = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
mismatches = 3

patternMatching(pattern, genome, mismatches)
