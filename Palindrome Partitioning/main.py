# Palindrome Partitioning

# Using Recursive Approach with Memoization (Top Down)

"""
Problem Statement:
    Given a String x = "abdbc"
    We have to partition the string in such a way that all the partition ara palindrome
    Return the minimum partition we require to do so
"""

# Input
string = "abdbc"

m = [[-1] * (len(string) + 1) for _ in range(len(string) + 1)]  # make a matrix for top down


# check whether string is palindrome or nto
def isPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


# define the main function
def solve(s, i, j):
    if i > j:  # Base condition
        return 0

    if m[i][j] != -1:  # No need to move ahead if we already calculated this part earlier
        return m[i][j]

    if isPalindrome(s, i, j):  # Another base Consition
        return 0

    minimum = float("inf")

    for k in range(i, j):
        if m[i][k] != -1:
            left = m[i][k]
        else:
            left = solve(s, i, k)

        if m[k + 1][j] != -1:
            right = m[k + 1][j]
        else:
            right = solve(s, k + 1, j)

        temp = left + right + 1
        minimum = min(temp, minimum)
    m[i][j] = minimum
    return m[i][j]


if __name__ == "__main__":
    ans = solve(string, 0, len(string) - 1)

    print(ans)  # print min no of partition we need
