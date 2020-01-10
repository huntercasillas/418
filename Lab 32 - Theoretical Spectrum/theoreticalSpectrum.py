# Hunter Casillas

table = {
    'A': 71, 'R': 156, 'N': 114, 'D': 115, 'C': 103, 'E': 129, 'Q': 128, 'G': 57, 'H': 137,
    'I': 113, 'L': 113, 'K': 128, 'M': 131, 'F': 147, 'P': 97, 'S': 87, 'T': 101, 'W': 186,
    'Y': 163, 'V': 99
}


def add_mass(subpeptide, masses):
    mass = 0
    for i in subpeptide:
        mass += table.get(i)
    masses += [mass]


def cyclospectrum(peptide):
    spectrum = [0]

    for i in range(1, len(peptide)):
        for j in range(len(peptide)):
            subpeptide = ""
            end = i if i <= len(peptide) - j else len(peptide) - j
            last = i - end
            subpeptide += peptide[j:j + end]
            subpeptide += peptide[0:last]
            add_mass(subpeptide, spectrum)
    spectrum.sort()
    add_mass(peptide, spectrum)

    return spectrum


def get_input(filename):
    file = open(filename, 'r')
    data = file.read().strip()
    return data


input = get_input("rosalind_ba4c.txt")
answer = cyclospectrum(input)
print(' '.join([str(x) for x in answer]))
