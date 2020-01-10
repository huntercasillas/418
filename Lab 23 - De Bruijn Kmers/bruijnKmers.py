# Hunter Casillas

def bruijn_kmers(kmers):
    dictionary = dict()
    for kmer in kmers:
        if kmer[:-1] in dictionary:
            dictionary[kmer[:-1]].append(kmer[1:])
            dictionary[kmer[:-1]].sort()

        else:
            dictionary[kmer[:-1]] = [kmer[1:]]

    graph = [' -> '.join([item[0], ','.join(item[1])]) for item in dictionary.items()]
    return graph


def get_input(filename):
    file = open(filename, 'r')
    data = file.read().splitlines()
    kmers = []
    for line in data:
        kmers.append(line)

    return kmers

kmers = get_input("rosalind_ba3e.txt")
answer = bruijn_kmers(kmers)
print("\n".join(answer))
