# Hunter Casillas

from functools import reduce

def eulerian_cycle(edges):
    for edge in edges:
        node = edge
        break

    path = [node]

    while True:
        path.append(edges[node][0])

        if len(edges[node]) == 1:
            del edges[node]
        else:
            edges[node] = edges[node][1:]

        if path[-1] in edges:
            node = path[-1]
        else:
            break

    while len(edges) > 0:
        for i in range(len(path)):
            if path[i] in edges:
                node = path[i]
                cycle = [node]
                while True:
                    cycle.append(edges[node][0])

                    if len(edges[node]) == 1:
                        del edges[node]
                    else:
                        edges[node] = edges[node][1:]

                    if cycle[-1] in edges:
                        node = cycle[-1]
                    else:
                        break

                path = path[:i] + cycle + path[i+1:]
                break
    return path


def eulerian_path(edges):
    output = reduce(lambda a, b: a + b, edges.values())

    for node in set(output + list(edges.keys())):
        out_val = output.count(node)
        if node in edges:
            in_val = len(edges[node])
        else:
            in_val = 0

        if in_val < out_val:
            unbalanced_from = node
        elif out_val < in_val:
            unbalanced_to = node

    if unbalanced_from in edges:
        edges[unbalanced_from].append(unbalanced_to)
    else:
        edges[unbalanced_from] = [unbalanced_to]

    cycle = eulerian_cycle(edges)

    divide = list(filter(lambda i: cycle[i:i + 2] == [unbalanced_from, unbalanced_to], range(len(cycle) - 1)))[0]

    return cycle[divide + 1:] + cycle[1:divide + 1]


def get_input(filename):
    file = open(filename, 'r')
    setup = []
    for line in file:
        setup.append(line.strip().split(' -> '))

    graph = {}
    for item in setup:
        graph[item[0]] = item[1].split(',')

    return graph


edges = get_input("rosalind_ba3g.txt")
answer = eulerian_path(edges)
print("->".join(map(str,answer)))
