# Hunter Casillas

def bruijn_string(text, k):
    dictionary = dict()

    for kmer in (text[i:i+k] for i in range(len(text)-k+1)):
        if kmer[:-1] in dictionary:
            dictionary[kmer[:-1]].add(kmer[1:])
        else:
            dictionary[kmer[:-1]] = {kmer[1:]}

    graph = [' -> '.join([item[0], ','.join(item[1])]) for item in dictionary.items()]
    return graph


def get_input(filename):
    file = open(filename, 'r')
    k = int(file.readline().strip())
    dna = str(file.readline().strip())
    return dna, k

dna, k = get_input("rosalind_ba3d.txt")
answer = bruijn_string(dna, k)
print("\n".join(answer))
