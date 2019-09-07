# Hunter Casillas

def frequentWords(input, length):
    dict = {}
    inputSize = len(input)
    for i in range(inputSize-length+1):
        slice = input[i:i+length]
        if dict.get(slice, 0) == 0:
            dict[slice] = 1
        else:
            dict[slice] = dict[slice]+1

    maximum = 0
    for i in dict:
        if dict[i] > maximum:
            maximum = dict[i]
    for i in dict:
        if dict[i] == maximum:
            print(i)


input = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
length = 4

frequentWords(input, length)
