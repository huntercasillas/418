# Hunter Casillas

def suffix_array(suffix):
    length = len(suffix)
    order = sort_characters(suffix)
    character_class = get_class(suffix, order)
    last = 1
    while last < length:
        order = sort_suffix(suffix, last, order, character_class)
        character_class = update_class(order, character_class, last)
        last = 2 * last
    return order


def sort_characters(suffix):
    length = len(suffix)
    order = [0] * length
    count = dict()
    for i in range(length):
        count[suffix[i]] = count.get(suffix[i], 0) + 1
    characters = sorted(count.keys())
    previous = characters[0]
    for char in characters[1:]:
        count[char] += count[previous]
        previous = char
    for i in range(length - 1, -1, -1):
        current = suffix[i]
        count[current] = count[current] - 1
        order[count[current]] = i
    return order


def get_class(suffix, order):
    length = len(suffix)
    character_class = [0] * length
    character_class[order[0]] = 0
    for i in range(1, length):
        if suffix[order[i]] != suffix[order[i - 1]]:
            character_class[order[i]] = character_class[order[i - 1]] + 1
        else:
            character_class[order[i]] = character_class[order[i - 1]]
    return character_class


def sort_suffix(suffix, last, order, character_class):
    length = len(suffix)
    count = [0] * length
    updated = [0] * length
    for i in range(length):
        count[character_class[i]] += 1
    for j in range(1, length):
        count[j] += count[j - 1]
    for i in range(length - 1, -1, -1):
        start = (order[i] - last + length) % length
        current = character_class[start]
        count[current] -= 1
        updated[count[current]] = start
    return updated


def update_class(order, character_class, last):
    n = len(order)
    updated = [0] * n
    updated[order[0]] = 0
    for i in range(1, n):
        current = order[i]
        previous = order[i - 1]
        middle = current + last
        previous_middle = (previous + last) % n
        if character_class[current] != character_class[previous] \
                or character_class[middle] != character_class[previous_middle]:
            updated[current] = updated[previous] + 1
        else:
            updated[current] = updated[previous]
    return updated


def burrows_wheeler(text, order):
    length = len(text)
    bwt = [''] * length
    nucleotides = ['$', 'A', 'C', 'G', 'T']
    for i in range(length):
        bwt[i] = text[(order[i] + length - 1) % length]

    count_dict = dict()
    start_dict = dict()
    for nucleotide in nucleotides:
        count_dict[nucleotide] = [0] * (length + 1)
    for i in range(length):
        current = bwt[i]
        for nucleotide, count in count_dict.items():
            count_dict[nucleotide][i + 1] = count_dict[nucleotide][i]
        count_dict[current][i + 1] += 1
    index = 0
    for nucleotide in sorted(nucleotides):
        start_dict[nucleotide] = index
        index += count_dict[nucleotide][length]
    return bwt, start_dict, count_dict
    

def suffix_matching(text, patterns, suffix):
    bwt, starts, counts = burrows_wheeler(text, suffix)
    answer = set()
    for pattern in patterns:
        top = 0
        bottom = len(bwt) - 1
        current = len(pattern) - 1
        while top <= bottom:
            if current >= 0:
                symbol = pattern[current]
                current -= 1
                if counts[symbol][bottom + 1] - counts[symbol][top] > 0:
                    top = starts[symbol] + counts[symbol][top]
                    bottom = starts[symbol] + counts[symbol][bottom + 1] - 1
                else:
                    break
            else:
                for i in range(top, bottom + 1):
                    answer.add(suffix[i])
                break
    return answer


def get_input(filename):
    file = open(filename, 'r')
    data = file.read().strip().split()
    text, patterns = data[0] + '$', data[1:]
    return text, patterns


text, patterns = get_input("rosalind_ba9h.txt")
suffix = suffix_array(text)
answer = suffix_matching(text, patterns, suffix)
print(' '.join(map(str, sorted(answer))))
