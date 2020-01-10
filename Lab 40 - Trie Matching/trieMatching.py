# Hunter Casillas

def trie_construction(patterns):
    trie = dict()
    trie[0] = dict()
    node = 1
    for pattern in patterns:
        pattern += '$'
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


def trie_prefix(text, trie):
    i = 0
    length = len(text)
    symbol = text[i]
    leaf = 0
    while True:
        if '$' in trie[leaf]:
            return True
        elif symbol in trie[leaf]:
            leaf = trie[leaf][symbol]
            if i < length - 1:
                i += 1
                symbol = text[i]
            elif not '$' in trie[leaf]:
                return False
        else:
            return False


def matching(text, patterns):
    result = []
    trie = trie_construction(patterns)
    for i in range(len(text)):
        if trie_prefix(text[i:], trie):
            result.append(i)
    return result


def get_input(filename):
    file = open(filename, 'r')
    data = []
    for line in file:
        data.append(line.strip())
    text = data[0]
    patterns = data[1:]
    return text, patterns


text, patterns = get_input("rosalind_ba9b.txt")
position = matching(text, patterns)
print(' '.join(map(str, position)))
