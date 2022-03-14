# Scramble String

"""
Problem Statement :
    Given two String A and B.
    You have to return True if B is a scramble string of A else return False

"""


def solve(a, b, dict):
    # Base condition
    if a == b:
        return True
    if len(a) <= 1:
        return False

    # define a key for storing in dictionary
    key = a + " " + b
    if dict.get(key, -1) != -1: # if key already present means we have already solve that part, just return it
        return dict[key]

    status = False
    n = len(a)
    for i in range(1, n):
        # condition1 = solve(a[:i], b[n - i:n], dict) and solve(a[i:n], b[:n - i], dict)
        condition1 = solve(a[:-i], b[i:], dict) and solve(a[-i:], b[:i], dict)
        condition2 = solve(a[:i], b[:i], dict) and solve(a[i:], b[i:], dict)
        if condition2 or condition1:
            status = True
            break

    dict[key] = status
    return dict[key]


if __name__ == '__main__':

    # Input :
    a = "great"
    b = "rgeat"
    dict = {}
    # Some Base condition
    if len(a) != len(b) or len(set(a)) != len(set(a)): # condition 1
        print("False")

    if a == "" and b == "": # condition 2
        print("True")

    if a == b: # condition 3
        print("True")

    res = solve(a, b, dict) # calling the function

    print(res) # printing the result
