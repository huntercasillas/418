# Hunter Casillas

def hammingDistance(p, q):
    distance = 0
    
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1

return distance

p = "GGGCCGTTGGT"
q = "GGACCGTTGAC"


print(hammingDistance(p, q))
