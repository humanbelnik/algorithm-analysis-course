
from matrix.matrix import matrix_init

def levensteinTrace(matrix, s1, s2):
    operations = []
    i, j = len(s1), len(s2)

    while i > 0 or j > 0:        
        if i > 0 and j > 0 and matrix[i][j] == matrix[i-1][j-1]:
            operations.append(f"M")
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j] == matrix[i - 1][j - 1] + 1:
            operations.append(f"R")
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + 1:
            operations.append(f"D")
            i -= 1
        else:
            operations.append(f"I")
            j -= 1

    return operations[::-1] 

def levenstein(s1, s2: str):
    l1, l2 = len(s1), len(s2)
    distance_matrix = matrix_init(l1 + 1, l2 + 1)

    for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                delta = 0 if s1[i - 1] == s2[j - 1] else 1
                distance_matrix[i][j] = min(distance_matrix[i - 1][j] + 1, distance_matrix[i][j - 1] + 1, distance_matrix[i - 1][j - 1] + delta)

    return distance_matrix[l1][l2], distance_matrix
                

def damerau_levenstein(s1, s2: str):
    l1, l2 = len(s1), len(s2)
    distance_matrix = matrix_init(l1 + 1, l2 + 1)

    for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                delta = 0 if s1[i - 1] == s2[j - 1] else 1
                distance_matrix[i][j] = min(distance_matrix[i - 1][j] + 1, distance_matrix[i][j - 1] + 1, distance_matrix[i - 1][j - 1] + delta)

                if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                    distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i - 2][j - 2] + 1)

    return distance_matrix[l1][l2], distance_matrix

        
def levenstein_recursive(s1, s2: str):  
    l1, l2 = len(s1), len(s2)

    if l1 == 0: return l2
    if l2 == 0: return l1

    delta = 0 if s1[l1 - 1] == s2[l2 - 1] else 1

    d = levenstein_recursive(s1[:l1 - 1], s2[:l2]) + 1
    i = levenstein_recursive(s1[:l1], s2[:l2 - 1]) + 1
    r = levenstein_recursive(s1[:l1 - 1], s2[:l2 - 1]) + delta

    dist = min(d, i, r)

    return dist

def damerau_levenstein_recursive(s1, s2: str):  
    l1, l2 = len(s1), len(s2)

    if l1 == 0: return l2
    if l2 == 0: return l1

    delta = 0 if s1[l1 - 1] == s2[l2 - 1] else 1

    d = damerau_levenstein_recursive(s1[:l1 - 1], s2[:l2]) + 1
    i = damerau_levenstein_recursive(s1[:l1], s2[:l2 - 1]) + 1
    r = damerau_levenstein_recursive(s1[:l1 - 1], s2[:l2 - 1]) + delta

    dist = min(d, i, r)
    if l1 > 1 and l2 > 1 and s1[l1 - 1] == s2[l2 - 2] and s1[l1 - 2] == s2[l2 - 1]:
        s = damerau_levenstein_recursive(s1[:l1 - 2], s2[:l2 -2]) + 1
        dist = min(dist, s)

    return dist


def damerau_levenstein_memo(s1, s2: str):
    memo = {}

    def f(s1, s2: str, memo: dict):
        l1, l2 = len(s1), len(s2)
        if (l1, l2) in memo:
             return memo[(l1, l2)]
        
        dist = damerau_levenstein_recursive(s1, s2)
        memo[(s1,s2)] = dist
        return dist

    return f(s1, s2, memo)
        
