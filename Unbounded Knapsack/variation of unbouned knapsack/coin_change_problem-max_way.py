# Coin change Problem
# Given a list/array of coin and money
# Return the max no. of ways that we can use coin to make same money

def find_zero(coin):
    return len([x for x in coin if x == 0])


def coin_change(coins, t):
    n = len(coins)
    m = [[0] * (t + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        m[i][0] = 2 ** find_zero(coins[:i])

    for i in range(1, n + 1):
        for j in range(1, t + 1):
            if coins[i - 1] <= j:
                m[i][j] = m[i][j - coins[i - 1]] + m[i - 1][j]
            else:
                m[i][j] = m[i - 1][j]
    return m[n][t]


# input
coins = [1, 2, 5]
money = 5

ways = coin_change(coins, money)

print(ways)