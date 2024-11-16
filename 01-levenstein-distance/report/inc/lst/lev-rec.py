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
