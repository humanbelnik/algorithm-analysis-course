from typing import List

def matrix_init(l1, l2: int) -> List[List[int]]:
    m =[[0 for _ in range(l2)] for _ in range(l1)]

    for i in range(l1):
        m[i][0] = i
    
    for i in range(l2):
        m[0][i] = i

    return m

def matrix_print(m: List[List[int]], prompt=">>"):
    print(prompt)
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            if j < len(m[i]) - 1:
                print(m[i][j], end=" ")  
            else:
                print(m[i][j])