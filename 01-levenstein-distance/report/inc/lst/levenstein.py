def levenstein(s1, s2: str):
    l1, l2 = len(s1), len(s2)
    distance_matrix = matrix_init(l1 + 1, l2 + 1)

    for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                delta = 0 if s1[i - 1] == s2[j - 1] else 1
                distance_matrix[i][j] = min(distance_matrix[i - 1][j] + 1, distance_matrix[i][j - 1] + 1, distance_matrix[i - 1][j - 1] + delta)

    return distance_matrix[l1][l2], distance_matrix