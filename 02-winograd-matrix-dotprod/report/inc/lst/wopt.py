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

