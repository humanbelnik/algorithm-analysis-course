def linear_search(data, x):
    n = len(data)
    ans=None
    for i in range(n):
        if data[i]==x:
            ans=i
            break
    return ans
