# Longest Common Substring
# Problem Statement :
# Given : Given two String string1 and string2
# Return : length of longest common substring


def lcs_substring(x, y):
    n1 = len(x)
    n2 = len(y)
    m = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if x[i - 1] == y[j - 1]:
                m[i][j] = m[i - 1][j - 1] + 1
            else:
                m[i][j] = 0

    # Finding the maximum length in matrix 
    mx = 0
    for i in m:
        mx = max(max(i), mx)
    return mx


# Input
string1 = "abcde"
string2 = "abfce"

length = lcs_substring(string1, string2)  # calling the function

print(length)  # printing the length of longest common substring
