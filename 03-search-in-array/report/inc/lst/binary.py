def binary_search(data, x):
    ans=None
    data.sort() 

    l = 0
    r = len(data) - 1

    while l <= r:
        i_pivot = (l + r) // 2
        pivot = data[i_pivot]

        if x == pivot:
            ans=i_pivot
            break
        elif x > pivot:
            l = i_pivot + 1
        else:
            r = i_pivot - 1

    return ans