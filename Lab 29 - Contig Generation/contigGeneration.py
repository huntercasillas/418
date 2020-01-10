# Hunter Casillas

def maximal_paths(graph):
    inner = dict()
    outer = dict()
    for w, vlist in graph.items():
        inner[w] = inner.get(w, 0)
        for v in vlist:
            inner[v] = inner.get(v, 0) + 1
        outer[w] = len(vlist)
    paths = []
    nodes = set()
    explored = set()
    for v in graph.keys():
        if not (1 == inner[v] and 1 == outer[v]):
            if outer[v] > 0:
                for w in graph[v]:
                    non_branching = [v, w]
                    while 1 == inner[w] and 1 == outer[w]:
                        explored.add(w)
                        u = graph[w][0]
                        non_branching.append(u)
                        w = u
                    paths.append(non_branching)
        else:
            nodes.add(v)
    for v in nodes:
        if v not in explored:
            w = v
            non_branching = []
            while w in nodes:
                non_branching.append(w)
                if w == v and len(non_branching) > 1:
                    paths.append(non_branching)
                    for node in non_branching:
                        explored.add(node)
                    break
                w = graph[w][0]
    return paths


def de_bruijn(k, patterns):
    bruijn = dict()
    for pattern in patterns:
        pl = pattern[:k - 1]
        pr = pattern[1:]
        if pl in bruijn:
            bruijn[pl].append(pr)
        else:
            bruijn[pl] = []
            bruijn[pl].append(pr)
        if pr not in bruijn:
            bruijn[pr] = []
    return bruijn


def contig_reconstruction(paths):
    contigs = []
    for path in paths:
        contigs.append(path[0] + ''.join([seq[-1] for seq in path[1:]]))
    return contigs

def get_input(filename):
    file = open(filename, 'r')
    data = file.read().strip().split()
    k = len(data[0])
    patterns = de_bruijn(k, data)
    return patterns


graph = get_input("rosalind_ba3k.txt")
paths = maximal_paths(graph)
answer = contig_reconstruction(paths)
print(' '.join(answer))

