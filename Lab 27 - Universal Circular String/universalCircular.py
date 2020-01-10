# Hunter Casillas

def universal_circular(k, n):
    alphabet = list(map(str, range(k)))
    a = [0] * k * n
    sequence = []

    def find(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            find(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                find(t + 1, t)
    find(1, 1)
    return "".join(alphabet[i] for i in sequence)


k = 9
answer = universal_circular(2, k)
print(answer)
