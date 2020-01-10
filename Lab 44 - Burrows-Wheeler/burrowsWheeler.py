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


def burrows_wheeler(text, suffix):
    return ''.join([text[(suffix[i] + len(text) - 1) % len(text)] for i in range(len(text))])


def get_input(filename):
    file = open(filename, 'r')
    text = file.read().strip()
    return text

text = get_input("rosalind_ba9i.txt")
suffix = suffix_array(text)
answer = burrows_wheeler(text, suffix)
print(answer)
