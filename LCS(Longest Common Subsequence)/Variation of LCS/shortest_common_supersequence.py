# Shortest Common Subsequence
# Problem Statement
# Given two string as usual string1 and string2
# Return length of shortest common supersequence

import print_lcs

#defining the function
def scs(x,y):
    # First of all find the LCS how would yu find that
    # 1 way to include that function
    # 2 way do it yourself
    lcs = print_lcs.find_lcs(x,y)
    return len(x)+len(y) - len(lcs)


# Input
string1 = "geek"
string2 = "eke"


if __name__ == "__main__":
    # Calling the function
    length = scs(string1,string2)
    #printing the length of shortest common supersequence (SCS)
    print(length)