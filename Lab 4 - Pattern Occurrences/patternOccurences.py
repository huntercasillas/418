# Hunter Casillas

import regex as re

def patternOccurences(pattern, genome):

    matches = re.finditer(pattern, genome, overlapped = True)

    for match in matches:
        print(match.start())


pattern = "ATAT"
genome = "GATATATGCATATACTT"

patternOccurences(pattern, genome) 
