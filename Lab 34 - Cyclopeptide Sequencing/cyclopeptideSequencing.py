# Hunter Casillas

def expand(peptides):
    masses = get_mass()
    expanded = set()
    for peptide in peptides:
        if '' == peptide:
            for mass in masses:
                expanded.add(mass)
        else:
            for mass in masses:
                expanded.add(peptide + '-' + mass)
    return expanded


def get_mass():
    mass = "57 71 87 97 99 101 103 113 114 115 128 129 131 137 147 156 163 186"
    return mass.split()


def calc_mass(peptide):
    return sum([int(a) for a in peptide.split('-')])


def linear(amino_acids):
    length = len(amino_acids)
    prefix = [0]
    for i in range(length):
        prefix.append(prefix[i] + amino_acids[i])
    linear_spectrum = [0]
    for i in range(length):
        for j in range(i + 1, length + 1):
            linear_spectrum.append(prefix[j] - prefix[i])
    current_dict = dict()
    for s in linear_spectrum:
        current_dict[s] = current_dict.get(s, 0) + 1
    return current_dict


def cyclospectrum(amino_acids):
    length = len(amino_acids)
    prefix = [0]
    for i in range(length):
        prefix.append(prefix[i] + amino_acids[i])
    peptide_mass = prefix[length]
    cyclo_spectrum = [0]
    for i in range(length):
        for j in range(i + 1, length + 1):
            cyclo_spectrum.append(prefix[j] - prefix[i])
            if i > 0 and j < length:
                cyclo_spectrum.append(peptide_mass - (prefix[j] - prefix[i]))
    current_dict = dict()
    for s in cyclo_spectrum:
        current_dict[s] = current_dict.get(s, 0) + 1
    return current_dict


def consistent_cyclo(peptide):
    amino_acids = [int(a) for a in peptide.split('-')]
    if cyclospectrum(amino_acids) == spectrum:
        return True
    else:
        return False


def consistent(peptide):
    amino_acids = [int(a) for a in peptide.split('-')]
    current_dict = linear(amino_acids)
    for key, value in current_dict.items():
        if value > spectrum.get(key, 0):
            return False
    return True


def sequence():
    peptides = {''}
    result = []
    while len(peptides) > 0:
        peptides = expand(peptides)
        deletions = []
        for peptide in peptides:
            if calc_mass(peptide) == parent:
                if consistent_cyclo(peptide):
                    result.append(peptide)
                deletions.append(peptide)
            elif not consistent(peptide):
                deletions.append(peptide)
        for peptide in deletions:
            peptides.remove(peptide)
    return result


def get_input(filename):
    file = open(filename, 'r')
    data = [int(n) for n in list(file.read().strip().split())]
    return data


spectrum = {}
input = get_input("rosalind_ba4e.txt")
parent = max(input)
for number in input:
    spectrum[number] = spectrum.get(number, 0) + 1

print(' '.join(sequence()))
