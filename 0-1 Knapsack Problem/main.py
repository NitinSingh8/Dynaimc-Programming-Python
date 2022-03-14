def knapsack(wt, val, n, w):
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if wt[i - 1] <= j:
                m[i][j] = max(val[i - 1] + m[i - 1][j - wt[i - 1]], m[i - 1][j])
            else:
                m[i][j] = m[i - 1][j]

    return m[n][w]


# input

wt_arr = [1, 3, 4, 5]
val_arr = [1, 4, 5, 7]
weight = 7
n = len(wt_arr)
m = [[0] * (weight + 1)] * (n + 1)

profit = knapsack(wt_arr, val_arr, n, weight)
print(profit)
