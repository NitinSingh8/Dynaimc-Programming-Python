# LCS (Longest Common Subsequence)

# Problem statement Given two string string1 and string2 . Your task is to find out longest common subsequence from them


# Approach1 (Recursive worst complexity)
def lcs(s1, s2):
    if s1 == "" or s2 == "":  # base condition
        return 0

    # recursive calling
    if s1[-1] == s2[-1]:
        return lcs(s1[:-1], s2[:-1]) + 1
    else:
        return max(lcs(s1[:-1], s2), lcs(s1, s2[:-1]))


# input
string1 = "COMPUTATIONAL"
string2 = "FUNCTIONAL"


number = lcs(string1, string2)  # calling the function

print(number)  # printing the len of longest common subsequence

# Approach 2 (Memoizatation) best for complexity

d = {}  # Or you can take here 2D list like d = [[-1]*(len(s2+1) for _ in range(s1+1)]


def lcs_with_memoizatation(s1, s2):
    if s1 == "" or s2 == "":
        return 0

    if d.get((s1, s2), -1) != -1:
        return d[(s1, s2)]

    if s1[-1] == s2[-1]:
        d[(s1, s2)] = lcs_with_memoizatation(s1[:-1], s2[:-1]) + 1

    else:
        d[(s1, s2)] = max(lcs_with_memoizatation(s1[:-1], s2), lcs_with_memoizatation(s1, s2[:-1]))
    return d[(s1, s2)]


number2 = lcs_with_memoizatation(string1, string2)
print(number2)


# Approach 3 ( Using Tabulation)

def lcs_with_tabulation(s1, s2):
    n = len(s1)
    n2 = len(s2)
    m = [[0] * (n2 + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                m[i][j] = m[i - 1][j - 1] + 1
            else:
                m[i][j] = max(m[i][j - 1], m[i - 1][j])


    for i in m:
        print(*i)
    return m[n][n2]


number3 = lcs_with_tabulation(string1, string2)

print(number3)
