# Rope Cutting Problem


def rope_cutting(length, price, N):
    n = len(length)
    m = [[0] * (N + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, N + 1):
            if length[i - 1] <= j:
                m[i][j] = max(price[i - 1] + m[i][j - length[i - 1]], m[i - 1][j])
            else:
                m[i][j] = m[i - 1][j]
    return m[n][N]


# Input
length = [1, 2, 3, 4, 5, 6, 7, 8]
price = [1, 5, 8, 9, 10, 17, 17, 20]
N = 8

maximum_profit = rope_cutting(length, price, N)

print(maximum_profit)
