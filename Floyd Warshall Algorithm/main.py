# Floyd Warshall Algorithm
"""
Problem Statement:
    Find the all pair shortest path in directed weightage graph
"""


def solution(adjacent_matrix):
    R_matrix = [row[:] for row in adjacent_matrix]

    n = len(R_matrix)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                R_matrix[j][k] = min(R_matrix[j][k], R_matrix[j][i] + R_matrix[i][k])

    return R_matrix


if __name__ == "__main__":

    # Input
    inf = float("inf")
    adjacent_matrix = [[0, 5, inf, 10],
                       [inf, 0, 3, inf],
                       [inf, inf, 0, 1],
                       [inf, inf, inf, 0]]
    # OR other test case
    # adjacent_matrix = [[0, 15, inf, inf],
    #                    [10, 0, 5, 15],
    #                    [20, inf, 0, 5],
    #                    [5, inf, 15, 0]]

    res = solution(adjacent_matrix)

    # printing the resultant matrix
    for row in res:
        for i in row:
            if i == inf:
                print("inf", end="  ")
            else:
                print(i, end="    ")
        print()
