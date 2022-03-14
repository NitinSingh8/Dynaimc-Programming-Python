def subset_sum(arr, n, s):
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if arr[i - 1] <= j:
                m[i][j] = (m[i - 1][j - arr[i - 1]]) or (m[i - 1][j])
            else:
                m[i][j] = m[i - 1][j]

    return m[n][s]


# input
arr = [2, 3, 5, 7, 8]
s = 4

n = len(arr)

# m[0][0] = True  # Intitalizing 0th column in matrix as True

m = [[0] * (s + 1) for i in range(n + 1)]

for i in range(n + 1):
    for j in range(s + 1):
        if i == 0:
            m[i][j] = False
        if j == 0:
            m[i][j] = True

result = subset_sum(arr, n, s)
print(result)
