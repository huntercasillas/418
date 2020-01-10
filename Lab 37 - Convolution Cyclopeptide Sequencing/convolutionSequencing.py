# Hunter Casillas

def get_mass():
    current_mass = '57 71 87 97 99 101 103 113 114 115 128 129 131 137 147 156 163 186'
    return current_mass.split()


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
    current_spectrum_dict = dict()
    for s in lSpectrum:
        current_spectrum_dict[s] = current_spectrum_dict.get(s, 0) + 1
    return current_spectrum_dict


def cyclospectrum(amino_acids):
    n = len(amino_acids)
    prefix_mass = [0]
    for i in range(n):
        prefix_mass.append(prefix_mass[i] + amino_acids[i])
    peptide_mass = prefix_mass[n]
    cyclo_spectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            cyclo_spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < n:
                cyclo_spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
    current_spectrum_dict = dict()
    for s in cyclo_spectrum:
        current_spectrum_dict[s] = current_spectrum_dict.get(s, 0) + 1
    return current_spectrum_dict


def consistent_cyclo(peptide):
    amino_acids = [int(a) for a in peptide.split('-')]
    if cyclospectrum(amino_acids) == spectrum_dict:
        return True
    else:
        return False


def consistent(peptide):
    amino_acids = [int(a) for a in peptide.split('-')]
    current_spectrum_dict = linear_spectrum(amino_acids)
    for key, value in current_spectrum_dict.items():
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


def spectral_convolution(spectrum, m):
    length = len(spectrum)
    convolution = dict()
    for i in range(length):
        for j in range(i + 1, length):
            current = spectrum[j] - spectrum[i]
            if 57 <= current:
                convolution[current] = convolution.get(current, 0) + 1
    sorted_mass = sorted(convolution.items(), key=lambda a: a[1], reverse=True)
    mass = [str(mass[0]) for mass in sorted_mass]
    multi = [mass[1] for mass in sorted_mass]
    num = multi[m - 1]
    for j in range(m, length):
        if multi[j] < num:
            return mass[:j]
    return mass


def calc_sequence_list(spectrum_dict, n):
    leaderboard = {''}
    leaderpeptide = ['']
    best = 0
    while len(leaderboard) > 0:
        leaderboard = expand(leaderboard)
        deletions = []
        for peptide in leaderboard:
            if calc_mass(peptide) == parent:
                currScore = cyclo_score(peptide, spectrum_dict)
                if currScore > best:
                    leaderpeptide = [peptide]
                    best = currScore
                elif currScore == best:
                    leaderpeptide.append(peptide)
            elif calc_mass(peptide) > parent:
                deletions.append(peptide)
        for p in deletions:
            leaderboard.remove(p)
        leaderboard = trim(leaderboard, spectrum_dict, n)
    return leaderpeptide


def get_input(filename):
    file = open(filename, 'r')
    M = int(file.readline().strip())
    N = int(file.readline().strip())
    data = [int(n) for n in file.read().strip().split()]
    return M, N, sorted(data)


spectrum_dict = dict()
m, n, spectrum = get_input('rosalind_ba4i.txt')
parent = max(spectrum)
for element in spectrum:
    spectrum_dict[element] = spectrum_dict.get(element, 0) + 1
spectral_mass = spectral_convolution(spectrum, m)
answer = calc_sequence_list(spectrum_dict, n)
print(' '.join(answer))
