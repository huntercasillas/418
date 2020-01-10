# Hunter Casillas

def profileMostKmer(text, k, matrix):
    dictionary = dict()
    kmer = text[0:len(k)]
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

def getInput(filename):
    file = open(filename, 'r')
    data = file.read().splitlines()
    input = []
    for line in data:
        input.append(line)

    dna = input[0]
    kmer = input[1]
    array = []

    for i in input[2:]:
        array.append(i)

    matrix = []
    for element in array:
        matrix.append(element.split(' '))

    return dna, kmer, matrix


dna, kmer, matrix = getInput("rosalind_ba2c.txt")
print(profileMostKmer(dna, kmer, matrix))
