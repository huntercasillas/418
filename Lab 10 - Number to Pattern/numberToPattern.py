# Hunter Casillas

def numberToSymbol(number):
    if number == 0:
        return 'A'
    elif number == 1:
        return 'C'
    elif number == 2:
        return 'G'
    elif number == 3:
        return 'T'
    else:
        return None


def numberToPattern(index, k):
    if k == 1:
        return numberToSymbol(index)
    
    quotient, remainder = divmod(index, 4)
    prefixPattern = numberToPattern(quotient, k-1)
    symbol = numberToSymbol(remainder)
    return prefixPattern + symbol


index = 45
k = 4

print(numberToPattern(index, k))
