# Print longest common subsequence

# Problem statement :
# Given two string s1 and s2 You have to writen longest common subsequence


def find_lcs(x, y):
    n1, n2 = len(x), len(y)
    m = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    # find the matrix (like same we do in LCS question)
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if x[i - 1] == y[j - 1]:
                m[i][j] = m[i - 1][j - 1] + 1
            else:
                m[i][j] = max(m[i - 1][j], m[i][j - 1])

    # After finding traverse from end and add string where it matching

    i, j, string = n1, n2, ""
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            string += x[i - 1]
            i -= 1
            j -= 1
        else:
            if m[i - 1][j] > m[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return string[::-1]


# Input
string1 = "abcdde"
string2 = "abdefc"

if __name__ == "__main__":

    lcs = find_lcs(string1, string2) # Calling the function

    print(lcs)  # longest Common Subsequence
