# Hunter Casillas

def hammingDistance(p, q):
    
    distance = 0
    pList = list(p)
    qList = list(q)
    
    for i in range(len(pList)):
        if pList[i] != qList[i]:
            distance += 1

print(distance)

p = "GGGCCGTTGGT"
q = "GGACCGTTGAC"


hammingDistance(p, q)
