# Hunter Casillas

def symbolToNumber(symbol):
    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    elif symbol == 'T':
        return 3
    else:
        return None


def patternToNumber(pattern):
    if len(pattern) == 0:
        return 0
    symbol = pattern[-1:]
    prefix = pattern[:-1]
    return 4 * patternToNumber(prefix) + symbolToNumber(symbol)


pattern = "AGT"

print(patternToNumber(pattern))
