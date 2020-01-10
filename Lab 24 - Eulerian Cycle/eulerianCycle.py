# Hunter Casillas

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


def get_input(filename):
    file = open(filename, 'r')
    setup = []
    for line in file:
        setup.append(line.strip().split(' -> '))

    graph = {}
    for item in setup:
        graph[item[0]] = item[1].split(',')

    return graph


edges = get_input("rosalind_ba3f.txt")
answer = eulerian_cycle(edges)
print("->".join(map(str,answer)))
