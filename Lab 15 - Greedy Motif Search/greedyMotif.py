# Hunter Casillas

def profileMostKmer(text, k, matrix):
    dictionary = dict()
    kmer = text[0:k]
    probable = 0
    k = int(k)
    end = len(text) - k
    for i in range(end):
        current = text[i:i + k]
        probability = compute(current, matrix)
        dictionary.update({current: probability})
        if probable < probability:
            probable = probability
            kmer = current

    return kmer

def compute(pattern, mat):
    probability = 1
    count = 0
    for i in range(len(pattern)):
        if pattern[i] == 'A':
            probability = probability * float(mat[0][count])
        elif pattern[i] == 'C':
            probability = probability * float(mat[1][count])
        elif pattern[i] == 'G':
            probability = probability * float(mat[2][count])
        elif pattern[i] == 'T':
            probability = probability * float(mat[3][count])

        count += 1

    return probability

def greedy(dna, k, t):
    bestMotifs = []
    matrixMotif = [[],[],[],[]]
    for element in dna:
        for i in range(len(element)):
            bestMotifs.append(element[i:i+k])
            break

    firstString = dna[0]
    motifArray = []
    for i in range(len(firstString) - k + 1):
        k_mer = firstString[i:i+k]
        motifArray = [k_mer]

        for j in range(1,t):
            matrixMotif = profile(motifArray)
            probKmer = profileMostKmer(dna[j],k,matrixMotif)
            motifArray.append(probKmer)

        if score(motifArray) < score(bestMotifs):
            bestMotifs = motifArray

    return bestMotifs

def profile(motifs):
    matrix = [[],[],[],[]]

    for i in range(len(motifs[0])):
        A = 0
        C = 0
        G = 0
        T = 0

        for element in motifs:
            if element[i] == 'A':
                A += 1
            elif element[i] == 'C':
                C += 1
            elif element[i] == 'G':
                G += 1
            elif element[i] == 'T':
                T += 1

        total = A + C + G + T
        matrix[0].append(float(A)/total)
        matrix[1].append(float(C)/total)
        matrix[2].append(float(G)/total)
        matrix[3].append(float(T)/total)


    return matrix

def score(patternMotif):
    currentScore = 0

    for i in range(len(patternMotif[0])):
        A = 0
        C = 0
        G = 0
        T = 0

        for element in patternMotif:
            if element[i] == 'A':
                A += 1
            elif element[i] == 'C':
                C += 1
            elif element[i] == 'G':
                G += 1
            elif element[i] == 'T':
                T += 1

        array = []
        array.append(A)
        array.append(C)
        array.append(G)
        array.append(T)

        maxNumber = max(array)
        total = A + C + G + T
        columnScore = total - maxNumber
        currentScore = currentScore + columnScore

    return currentScore

def getInput(filename):
    file = open(filename, 'r')
    k, t = file.readline().split()
    k = int(k)
    t = int(t)
    data = file.read().splitlines()
    input = []
    for line in data:
        input.append(line)

    return input, k, t


input = getInput("rosalind_ba2d.txt")
print(*greedy(input, 12, 25))
