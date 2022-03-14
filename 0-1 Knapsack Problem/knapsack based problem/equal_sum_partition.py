def equal_sum_partition(elements):
    s = sum(elements)
    n = len(elements)
    if s % 2 != 0:
        return False
    s //= 2

    m = [[False]*(s+1) for _ in range(n+1)]

    for i in range(n+1):
        m[i][0] = True

    for i in range(1,n+1):
        for j in range(1,s+1):
            if elements[i-1]<=j:
                m[i][j] = m[i-1][j-elements[i-1]] or m[i-1][j]
            else:
                m[i][j] = m[i-1][j]

    return m[n][s]


elements = [1, 3, 7, 5]
out = equal_sum_partition(elements)
print("possible") if out else print("not possible")
