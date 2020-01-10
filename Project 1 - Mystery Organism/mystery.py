# Hunter Casillas

from Bio import SeqIO

def minimumSkew(genome):
    positions = []
    minimum = 0
    skew = 0

    for index, character in enumerate(genome):
        if character == 'C':
            skew -= 1
        elif character == 'G':
            skew += 1

        if skew < minimum:
            minimum = skew
            positions.clear()
            positions.append(index + 1)
        elif skew == minimum:
            positions.append(index + 1)

    return positions



def hammingDistance(p, q):

    distance = 0
    pList = list(p)
    qList = list(q)

    for i in range(len(pList)):
        if pList[i] != qList[i]:
            distance += 1

    return distance


def neighbors(pattern,d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ['A','C','G','T']

    neighborhood = []
    suffixNeighbors = neighbors(pattern[1:],d)
    for text in suffixNeighbors:
        if hammingDistance(pattern[1:],text) < d:
            for x in ['A','C','G','T']:
                neighborhood.append(x+text)
        else:
            neighborhood.append(pattern[:1]+text)
    neighborhood = list(set(neighborhood))
    return neighborhood

def approximatePatternCount(text,pattern,d):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if hammingDistance(text[i:i+len(pattern)],pattern) <= d:
            count += 1
    return count

def symbolToNumber(symbol):
    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    elif symbol == 'T':
        return 3
    else:
        return None

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

def patternToNumber(pattern):
    if len(pattern) == 0:
        return 0
    symbol = pattern[-1:]
    prefix = pattern[:-1]
    return 4 * patternToNumber(prefix) + symbolToNumber(symbol)


def numberToPattern(index, k):
    if k == 1:
        return numberToSymbol(index)

    quotient, remainder = divmod(index, 4)
    prefixPattern = numberToPattern(quotient, k - 1)
    symbol = numberToSymbol(remainder)
    return prefixPattern + symbol

def reverse_complement(dna):
    dnadict = {'A':'T','C':'G','G':'C','T':'A'}
    reverseDna = [ dnadict[c] for c in dna ]
    return ''.join(reverseDna[::-1])

def frequentWordsWithMismatchesReverse(text, k, d):
    neighborhoods = []
    for i in range(len(text) - k + 1):
        reverseString = reverse_complement(text[i:i + k])
        neighborhoods = neighborhoods + neighbors(text[i:i + k], d) + neighbors(reverseString, d)

    count = [0] * len(neighborhoods)
    index = [0] * len(neighborhoods)
    for i in range(len(neighborhoods)):
        pattern = neighborhoods[i]
        index[i] = patternToNumber(pattern)
        count[i] = 1

    sortedIndex = sorted(index)
    for i in range(len(neighborhoods) - 1):
        if sortedIndex[i] == sortedIndex[i + 1]:
            count[i + 1] = count[i] + 1
    maxCount = max(count)
    frequentPatterns = [numberToPattern(sortedIndex[i], k) for i, c in enumerate(count) if c == maxCount]
    return frequentPatterns

def frequentWordsWithMismatches(text, k, d):
    frequentPatterns = []
    close = [0] * (4 ** k)
    frequencyArray = [0] * (4 ** k)
    for i in range(len(text) - k + 1):
        neighborhood = neighbors(text[i:i + k], d)
        for pattern in neighborhood:
            index = patternToNumber(pattern)
            close[index] = 1
    for i in range(4 ** k):
        if close[i] == 1:
            pattern = numberToPattern(i, k)
            frequencyArray[i] = approximatePatternCount(text, pattern, d)

    maxCount = max(frequencyArray)
    for i in range(4 ** k):
        if frequencyArray[i] == maxCount:
            pattern = numberToPattern(i, k)
            frequentPatterns.append(pattern)
    return list(set(frequentPatterns))


def readFasta(genome):
    for fasta in genome:
        name, sequence = fasta.id, str(fasta.seq)
        return sequence


ecoli_fasta = SeqIO.parse(open("ecoli.fasta"), 'fasta')
ecoli = readFasta(ecoli_fasta)

spooky_fasta = SeqIO.parse(open("notSoSpooky.fasta"), 'fasta')
spooky = readFasta(spooky_fasta)


print(minimumSkew(spooky))

ecoli_input = ecoli[3923620:(3923620+500)]
freq_ecoli = frequentWordsWithMismatchesReverse(ecoli_input, 9, 1)
print(freq_ecoli)


spooky_input = spooky[3744269:(3744269+500)]
spooky_input2 = spooky[(3744269-250):(3744269+250)]
spooky_input3 = spooky[(3744269-500):3744269]
spooky_input4 = spooky[3744269:(3744269+1000)]


freq_spooky = frequentWordsWithMismatchesReverse(spooky_input, 9, 1)
freq_spooky2 = frequentWordsWithMismatchesReverse(spooky_input2, 9, 1)
freq_spooky3 = frequentWordsWithMismatchesReverse(spooky_input3, 9, 1)
freq_spooky4 = frequentWordsWithMismatchesReverse(spooky_input4, 9, 1)


print(freq_spooky)
print(freq_spooky2)
print(freq_spooky3)
print(freq_spooky4)
