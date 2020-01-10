# Hunter Casillas

def form_graph(patterns):
    nodes = {}
    edges = {}
    for i in range(len(patterns)):
        nodes[i] = patterns[i]
        edges[i] = []
    return nodes,edges

def overlap(patterns):
    temp = []
    nodes,edges = form_graph(patterns)
    k = len(patterns[0])
    for i in range(len(patterns)):
        prefix = patterns[i][:k-1]
        nodes_in = [pat.find(prefix,1) for pat in patterns]
        nodes_in = [loc for loc,node in enumerate(nodes_in) if node >0]
        if len(nodes_in):
            for node in nodes_in:
                edges[node].append(i)
    for key, values in edges.items():
        if len(values):
            for val in values:
                temp.append(nodes[key] + ' -> ' + nodes[val])
    return temp

def get_input(filename):
    file = open(filename, 'r')
    data = file.read().splitlines()
    patterns = []
    for line in data:
        patterns.append(line)

    return patterns

patterns = sorted(get_input("rosalind_ba3c.txt"))
answer = overlap(patterns)
print("\n".join(answer))
