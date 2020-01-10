# Hunter Casillas

def convolution_list(spectrum):
    length = len(spectrum)
    convolution = []
    for i in range(length):
        for j in range(i + 1, length):
            current = spectrum[j] - spectrum[i]
            if current != 0:
                convolution.append(current)
    return convolution


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


def get_input(filename):
    file = open(filename, 'r')
    data = sorted([int(n) for n in file.read().strip().split()])
    return data


input = get_input('rosalind_ba4h.txt')
answer = convolution_list(input)
print(' '.join([str(n) for n in answer]))
