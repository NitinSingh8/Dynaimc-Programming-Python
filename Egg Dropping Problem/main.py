# Egg dropping Problem


"""
Problem Statement :
    Given a number (which define the total floor of building) and total number of eggs
    We have to find the top most floor number where we throw an egg and it doesn't break
    Now we have to return the minimum step we need to reach that floor

"""


def solve(egg,floor,matrix):
    if floor ==1 or floor ==0:
        return floor
    if egg==1:
        return floor

    if matrix[egg][floor]!=-1:
        return matrix[egg][floor]

    minimum = float("inf")
    for i in range(1,floor):

        if matrix[egg-1][i-1]!=-1:
            down = matrix[egg-1][i-1]
        else:
            down = solve(egg-1,i-1,matrix)

        if matrix[egg][floor-i]!=-1:
            up = matrix[egg][floor-i]
        else:
            up = solve(egg,floor-i,matrix)
        temp = 1 + max(down,up)

        minimum = min(temp,minimum)


    matrix[egg][floor]= minimum
    return matrix[egg][floor]




if __name__ == "__main__":
    # Input :
    floor = 10
    eggs = 2

    matrix = [[-1] * (floor + 1) for _ in range(eggs + 1)]

    res = solve(eggs, floor,matrix)  # Calling the floor

    print(res)  # print the minium step we need to reach required floor
