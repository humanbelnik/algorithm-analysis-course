from typing import List

Matrix = List[List[int]]

def read_matrix_from_file(f: str) -> Matrix:
    with open(f, 'r') as file:
        dimensions = file.readline().strip().split()
        rows = int(dimensions[0])
        
        m = []
        for _ in range(rows):
            row = list(map(int, file.readline().strip().split()))
            m.append(row)
        
        return m
    
def print_matrix(m: Matrix, prompt="Matrix:") -> None:
    print(prompt)
    for row in m:
        print(row)
    
def dotprod_std(a: Matrix, b: Matrix) -> Matrix: # 0
    n = len(a) 
    m = len(a[0])
    p = len(b[0])
    c = [[0] * p for _ in range(n)] 
    
    for i in range(n): 
        for j in range(p):
            for k in range(m):
                c[i][j] += a[i][k] * b[k][j] #   
    
    return c

def dotprod_winograd(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    m = len(a[0])
    p = len(b[0])

    row_factor = [0] * n
    col_factor = [0] * p

    for i in range(n): 
        for j in range(0, m // 2):
            row_factor[i] = row_factor[i] + a[i][2 * j] * a[i][2 * j + 1] 

    for i in range(p):
        for j in range(0, m // 2):
            col_factor[i] = col_factor[i] + b[2 * j][i] * b[2 * j + 1][i]

    c = [[0] * p for _ in range(n)]

    for i in range(n):
        for j in range(p):
            c[i][j] = -row_factor[i] - col_factor[j] # 7
            for k in range(0, m // 2):
                c[i][j] = c[i][j] + (a[i][2 * k] + b[2 * k + 1][j]) * (a[i][2 * k + 1] + b[2 * k][j]) 
    
    if m % 2 == 1:
        for i in range(n): 
            for j in range(p):
                c[i][j] = c[i][j] + a[i][m - 1] * b[m - 1][j]

    return c

def dotprod_winograd_optimized(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    m = len(a[0])
    p = len(b[0])

    row_factor = [0] * n
    col_factor = [0] * p

    for i in range(n): 
        for j in range(0, m - 1, 2): 
            row_factor[i] -= a[i][j] * a[i][j + 1] 
    for i in range(p):
        for j in range(0, m - 1, 2):  
            col_factor[i] -= b[j][i] * b[j + 1][i]

    c = [[0] * p for _ in range(n)]

    for i in range(n): 
        for j in range(p):
            c[i][j] = row_factor[i] + col_factor[j]
            for k in range(0, m - 1, 2): 
                c[i][j] += (a[i][k] + b[k + 1][j]) * (a[i][k + 1] + b[k][j]) 

    if m % 2 == 1:
        for i in range(n):
            for j in range(p):
                c[i][j] += a[i][m - 1] * b[m - 1][j]

    return c

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]



def strassen_matrix_multiply(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen_matrix_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = strassen_matrix_multiply(add_matrices(A21, A22), B11)
    M3 = strassen_matrix_multiply(A11, subtract_matrices(B12, B22))
    M4 = strassen_matrix_multiply(A22, subtract_matrices(B21, B11))
    M5 = strassen_matrix_multiply(add_matrices(A11, A12), B22)
    M6 = strassen_matrix_multiply(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = strassen_matrix_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))

    C11 = add_matrices(subtract_matrices(add_matrices(M1, M4), M5), M7)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = add_matrices(subtract_matrices(add_matrices(M1, M3), M2), M6)

    C = [[0] * n for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]

    return C