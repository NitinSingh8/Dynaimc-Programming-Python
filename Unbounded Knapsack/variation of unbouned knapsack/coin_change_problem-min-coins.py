# coin change problem - II

# Given list/array of coins and total amount
# return the min coins used to make that total amount

import sys


# 1. Approach without dynamic Programming
def coin_change(coins, amount):
    coins.sort(reverse=True)
    cnt = 0
    for i in coins:
        if amount == 0:
            break
        while (i <= amount):
            amount -= i
            cnt += 1
    return cnt


coins = [1, 2, 5]
amount = 2

coins_used = coin_change(coins, amount)
print("By approach 1st ", coins_used)


# 2. Approach With Dynamic Programming
def coin_change_with_dynamic(coins, a):
    n = len(coins)
    m = [[sys.maxsize - 1] * (a + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        m[i][0] = 0

    for j in range(1, a + 1):
        if coins[0] % j == 0:
            m[1][j] = coins[0] // j

        for i in range(1, n + 1):
            for j in range(1, a + 1):
                if coins[i - 1] <= j:
                    m[i][j] = min(m[i][j - coins[i - 1]] + 1, m[i - 1][j])
                else:
                    m[i][j] = m[i - 1][j]
        return m[n][a]


coin_used = coin_change_with_dynamic(coins, amount)
print("By approach 2nd : ", coin_used)
