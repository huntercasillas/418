# Hunter Casillas

def match(i, root, text):
    length = len(text)
    current_node = root
    at_node = True
    for j in range(i, length):
        if at_node:
            current_position = 0
            if not text[j] in tree[current_node]:
                return current_node, None, j, -1
            else:
                current_edge = tree[current_node][text[j]]
                current_string = current_edge.get_string()
                last_string = len(current_string) - 1
                if last_string == 0:
                    current_node = current_edge.end_node
                    continue
                else:
                    at_node = False
        else:
            current_position += 1
            if text[j] != current_string[current_position]:
                return current_node, current_edge, j, current_edge.start + current_position
            else:
                last_string -= 1
                if last_string == 0:
                    current_node = current_edge.end_node
                    at_node = True


def add(node, start, end, leaf):
    new_edge = Edge(start, end, text, node, None, leaf)
    tree[node][new_edge.get_start()] = new_edge


def split(edge, start, end, cut, leaf):
    new_node = Node()
    new_edge = Edge(start, end, text, new_node, None, leaf)
    tree[new_node] = dict()
    tree[new_node][new_edge.get_start()] = new_edge
    edge2 = Edge(cut, edge.end, text, new_node, edge.end_node)
    tree[new_node][edge2.get_start()] = edge2
    tree[edge.start_node][edge.get_start()].end = cut - 1
    tree[edge.start_node][edge.get_start()].end_node = new_node


def build(root, text):
    length = len(text)
    edge1 = Edge(0, length - 1, text, root)
    tree[root] = dict()
    tree[root][edge1.get_start()] = edge1
    for i in range(1, length):
        current_node, current_edge, j, cut = match(i, root, text)
        if not current_edge:
            add(current_node, j, length - 1, i)
        else:
            split(current_edge, j, length - 1, cut, i)


def explore(tree):
    results = []
    for node in tree.keys():
        for edge in tree[node].values():
            results.append(edge.get_string())
    return results


class Node:
    total = 0
    def __init__(self):
        Node.total += 1
        self.id = self.total


class Edge:
    def __init__(self, start, end, text, start_node, end_node = None, leaf = None):
        self.start = start
        self.end = end
        self.text = text
        self.start_node = start_node
        self.end_node = end_node
        self.leaf = leaf

    def get_length(self):
        return self.end - self.start + 1

    def get_string(self):
        return self.text[self.start:self.end + 1]

    def get_start(self):
        return self.text[self.start]


def get_input(filename):
    file = open(filename, 'r')
    data = file.read().strip().split()
    return data[0]


text = get_input("test.txt")
root = Node()
tree = dict()
build(root, text)
print('\n'.join(explore(tree)))
