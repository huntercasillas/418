# Hunter Casillas

def get_mass():
    mass = '57 71 87 97 99 101 103 113 114 115 128 129 131 137 147 156 163 186'
    return mass.split()


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


def calc_mass(peptide):
    return sum([int(a) for a in peptide.split('-')])


def linear_spectrum(amino_acids):
    n = len(amino_acids)
    PrefixMass = [0]
    for i in range(n):
        PrefixMass.append(PrefixMass[i] + amino_acids[i])
    lSpectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            lSpectrum.append(PrefixMass[j] - PrefixMass[i])
    currspectrum_dict = dict()
    for s in lSpectrum:
        currspectrum_dict[s] = currspectrum_dict.get(s, 0) + 1
    return currspectrum_dict


def cyclospectrum(amino_acids):
    n = len(amino_acids)
    PrefixMass = [0]
    for i in range(n):
        PrefixMass.append(PrefixMass[i] + amino_acids[i])
    peptideMass = PrefixMass[n]
    cSpectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            cSpectrum.append(PrefixMass[j] - PrefixMass[i])
            if i > 0 and j < n:
                cSpectrum.append(peptideMass - (PrefixMass[j] - PrefixMass[i]))
    currspectrum_dict = dict()
    for s in cSpectrum:
        currspectrum_dict[s] = currspectrum_dict.get(s, 0) + 1
    return currspectrum_dict


def consistent_cyclo(peptide):
    amino_acids = [int(a) for a in peptide.split('-')]
    if cyclospectrum(amino_acids) == spectrum_dict:
        return True
    else:
        return False


def consistent(peptide):
    amino_acids = [int(a) for a in peptide.split('-')]
    currspectrum_dict = linear_spectrum(amino_acids)
    for key, value in currspectrum_dict.items():
        if value > spectrum_dict.get(key, 0):
            return False
    return True


def linear_score(peptide, spectrum_dict):
    if 0 == len(peptide):
        return 0
    amino_acids = [int(a) for a in peptide.split('-')]
    theo_dict = linear_spectrum(amino_acids)
    score = 0
    for s, v in theo_dict.items():
        v0 = spectrum_dict.get(s, 0)
        if v0 >= v:
            score += v
        else:
            score += v0
    return score


def cyclo_score(peptide, spectrum_dict):
    if 0 == len(peptide):
        return 0
    amino_acids = [int(a) for a in peptide.split('-')]
    theo_dict = cyclospectrum(amino_acids)
    score = 0
    for s, v in theo_dict.items():
        v0 = spectrum_dict.get(s, 0)
        if v0 >= v:
            score += v
        else:
            score += v0
    return score


def trim(leaderboard, spectrum_dict, number):
    length = len(leaderboard)
    linear_score_dict = dict()
    for peptide in leaderboard:
        linear_score_dict[peptide] = linear_score(peptide, spectrum_dict)
    score = sorted(linear_score_dict.items(), key=lambda a: a[1], reverse=True)
    leaderboard = [p[0] for p in score]
    scores = [p[1] for p in score]
    for j in range(number, length):
        if scores[j] < scores[number - 1]:
            return leaderboard[:j]
    return leaderboard


def calc_sequence(spectrum_dict, number):
    leaderboard = {''}
    leaderpeptide = ''
    best = 0
    while len(leaderboard) > 0:
        leaderboard = expand(leaderboard)
        deletions = []
        for peptide in leaderboard:
            if calc_mass(peptide) == parent:
                current_score = cyclo_score(peptide, spectrum_dict)
                if current_score > best:
                    leaderpeptide = peptide
                    best = current_score
            elif calc_mass(peptide) > parent:
                deletions.append(peptide)
        for peptide in deletions:
            leaderboard.remove(peptide)
        leaderboard = trim(leaderboard, spectrum_dict, number)
    return leaderpeptide


def get_input(filename):
    file = open(filename, 'r')
    data = []
    for element in file:
        data.append(element.strip())
    num = int(data[0])
    data = [int(n) for n in data[1].strip().split()]
    parent = max(data)
    return num, data, parent


spectrum_dict = dict()
number, input, parent = get_input('rosalind_ba4g.txt')
for n in input:
    spectrum_dict[n] = spectrum_dict.get(n, 0) + 1
answer = calc_sequence(spectrum_dict, number)
print(answer)
