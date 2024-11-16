def dotprod_std(a: Matrix, b: Matrix) -> Matrix: 
    n = len(a) 
    m = len(a[0])
    p = len(b[0])
    c = [[0] * p for _ in range(n)] 
    
    for i in range(n): 
        for j in range(p):
            for k in range(m):
                c[i][j] += a[i][k] * b[k][j] #   
    
    return c