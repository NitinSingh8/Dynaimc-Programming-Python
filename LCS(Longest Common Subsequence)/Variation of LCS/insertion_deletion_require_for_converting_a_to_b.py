# Problem statement
# Given two string string1 and string2
# Return no of insertion no of deletion require to convert string1 to string2

import print_lcs


def get_insert_delete(x, y):
    # first find lcs of this two string x and y
    # then return the                deletion = len(x) - len(lcs)
    #                                insertion = len(y) - len(lcs)
    lcs = print_lcs.find_lcs(x, y)

    return len(y) - len(lcs), len(x) - len(lcs)


# Input
string1 = "heap"
string2 = "pea"

if __name__ == "__main__":
    insertion, deletion = get_insert_delete(string1, string2)  # calling the function

    # printing the output
    print("insertion require : ", insertion)
    print("deletion require : ", deletion)
