# Hunter Casillas

def trie_construction(patterns):
    trie = dict()
    trie[0] = dict()
    node = 1
    for pattern in patterns:
        current = 0
        for i in range(len(pattern)):
            symbol = pattern[i]
            if symbol in trie[current]:
                current = trie[current][symbol]
            else:
                trie[node] = dict()
                trie[current][symbol] = node
                current = node
                node += 1
    return trie


def get_input(filename):
    file = open(filename, 'r')
    patterns = []
    for line in file:
        patterns.append(line.strip())
    return patterns


patterns = get_input("rosalind_ba9a.txt")
trie = trie_construction(patterns)

for node in trie:
    for element in trie[node]:
        print('{}->{}:{}'.format(node, trie[node][element], element))
