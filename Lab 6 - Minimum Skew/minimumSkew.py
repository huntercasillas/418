# Hunter Casillas

def minimumSkew(genome):
    
    skewList = []
    skewAnswer = []
    for i in range(len(genome)):
        current = genome[i:len(genome)]
        count = current.count('C') - current.count('G')
        skewList.append(count)
    
    
    minSkew = min(skewList)
    for i in range(len(skewList)):
        if skewList[i] == minSkew:
            skewAnswer.append(str(i))

print(skewAnswer)


genome = "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"

minimumSkew(genome) 
