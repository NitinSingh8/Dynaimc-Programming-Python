# Boolean Parenthesization
'''
Problem Statement :
    Given a boolean expression containing T(True),F(False) , &(And operator) , | (Or Operator) and ^ (Xor Operator)
    We have to find maximum no of ways so that the the result of this expression become True
    Return that number of ways
'''

# Input:
string = "F|T|T&F^T"

# Here instead of making matrix we will make dictionary
dict = {}


# Function
def solve(s, i, j,
          status):  # Here initial i = 0 ,j = len(string) -1 and status = True(bcz we want no ways that expression come true)

    if i > j:  # Base Condition
        return 0

    if i == j:
        if status and s[i] == 'T':
            return 1
        elif status is False and s[i] == 'F':
            return 1
        else:
            return 0

    key = '{0} {1} {2}'.format(i, j, status)
    # print(key)
    if dict.get(key, -1) != -1:
        return dict[key]

    res = 0

    for k in range(i + 1, j, 2):
        key_lt = '{0} {1} {2}'.format(i, k-1, True)
        if dict.get(key_lt,-1)!=-1:
            lt = dict[key_lt]
        else:
            lt = solve(s, i, k - 1, True)

        key_lf = '{0} {1} {2}'.format(i, k - 1, False)
        if dict.get(key_lf, -1) != -1:
            lf = dict[key_lf]
        else:
            lf = solve(s, i, k - 1, False)

        key_rt = '{0} {1} {2}'.format(k+1,j, True)
        if dict.get(key_rt,-1)!=-1:
            rt = dict[key_rt]
        else:
            rt = solve(s, k+1, j, True)

        key_rf = '{0} {1} {2}'.format(k+1, j, False)
        if dict.get(key_rf, -1) != -1:
            rf = dict[key_rf]
        else:
            rf = solve(s, k+1,j, False)


        if s[k] == '^':
            if status:
                res = res + lf * rt + lt * rf
            else:
                res = res + lt * rt + lf * rf

        if s[k] == '&':
            if status:
                res = res + lt * rt
            else:
                res = res + lt * rf + lf * rt + lf * rf
        if s[k] == '|':
            if status:
                res = res + lt * rf + lf * rt + lt * rt
            else:
                res = res + lf * rf
    dict[key] = res
    return dict[key]


if __name__ == "__main__":
    ans = solve(string, 0, len(string) - 1, True)

    print(ans)  # Printing the number of ways
