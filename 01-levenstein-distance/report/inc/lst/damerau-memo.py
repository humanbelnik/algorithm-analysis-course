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
