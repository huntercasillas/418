# Hunter Casillas

def get_mass():
    mass = '57 71 87 97 99 101 103 113 114 115 128 129 131 137 147 156 163 186'
    return [int(m) for m in mass.split()]


def counting_peptides(n):
    masses = get_mass()
    length = len(masses)
    table = [0] * (n + 1)
    table[0] = 1
    for i in range(n + 1):
        current = 0
        for j in range(length):
            if i - masses[j] >= 0:
                current += table[i - masses[j]]
        table[i] += current
    return table[n]


def get_input(filename):
    file = open(filename, 'r')
    data = int(file.read().strip())
    return data


input = get_input("rosalind_ba4d.txt")
answer = counting_peptides(input)
print(answer)
