# Hunter Casillas

import math

def hamming_distance(str1, str2):
    counter = 0
    for s1, s2 in zip(str1, str2):
        if s1 != s2:
            counter += 1
    return counter

def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    distance = 0
    for string in dna:
        hammingdistance = math.inf
        for i in range(len(string) - k + 1):
            if hammingdistance > hamming_distance(pattern, string[i:i + k]):
                hammingdistance = hamming_distance(pattern, string[i:i + k])
        distance = distance + hammingdistance
    return distance

def get_input(filename):
    file = open(filename, 'r')
    pattern = file.readline().split()
    dna = file.readline().split()

    return pattern, dna

pattern, dna = get_input("rosalind_ba2h.txt")
data = "".join(open('rosalind_ba2h.txt')).split()

print(distance_between_pattern_and_strings(data[0], data[1:]))
