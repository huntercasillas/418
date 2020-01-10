# Hunter Casillas

def setup_bwt(bwt):
    length = len(bwt)
    count_dict = dict()
    start_dict = dict()
    nucleotides = ['$', 'A', 'C', 'G', 'T']
    for nucleotide in nucleotides:
        count_dict[nucleotide] = [0] * (length + 1)
    for i in range(length):
        current = bwt[i]
        for nucleotide, count in count_dict.items():
            count_dict[nucleotide][i+1] = count_dict[nucleotide][i]
        count_dict[current][i+1] += 1
    index = 0
    for nucleotide in sorted(nucleotides):
        start_dict[nucleotide] = index
        index += count_dict[nucleotide][length]
    return start_dict, count_dict


def better_matching(pattern, bwt, start_dict, count_dict):
    top = 0
    bottom = len(bwt) - 1
    index = len(pattern) - 1
    while top <= bottom:
        if index >= 0:
            symbol = pattern[index]
            index -= 1
            if count_dict[symbol][bottom + 1] - count_dict[symbol][top] > 0:
                top = start_dict[symbol] + count_dict[symbol][top]
                bottom = start_dict[symbol] + count_dict[symbol][bottom + 1] - 1
            else:
                return 0
        else:
            return bottom - top + 1


def get_input(filename):
    file = open(filename, 'r')
    data = file.read().strip().split()
    bwt = data[0]
    patterns = data[1:]
    return bwt, patterns

bwt, patterns = get_input("rosalind_ba9m.txt")
starts, occ_counts_before = setup_bwt(bwt)
occurrence_counts = []
for pattern in patterns:
    occurrence_counts.append(better_matching(pattern, bwt, starts, occ_counts_before))

print(' '.join(map(str, occurrence_counts)))
