# Matrix Chain Multiplication
# Using Recursive Code with Memoization  (Top Down)

'''
    Problem Statement :
              Given a array having dimesnion of matrix
              We have to do mulitplication of all matrix in such a way that cost become minium
              Return that cost

              how to find cost if we multiply two matrix :
                            Let Say there is two matrix A and B.
                                A = 3 * 4 (3 Row and 4 Column)
                                B = $ * 5 (4 Row and 5 Column)
                                Cose Would be 3*4*5 = 60
'''


# Input  : Given Array
arr = [10,20,30,40,30,50]

m = [[-1]*(len(arr) + 1) for _ in range(len(arr) + 1)]  # Make a matrix


def solve(arr, i, j):  # i = 1 , j = len(arr) -1

    if i >= j: # Base Condition
        return 0

    if m[i][j]!=-1:  # No need to move ahead if we already calculated this part earlier
        return m[i][j]

    minimum = float("inf")

    for k in range(i,j):

        if m[i][k]!=-1:
            left = m[i][k]
        else:
            left= solve(arr,i,k)

        if m[k+1][j]!=-1:
            right = m[k+1][j]
        else:
            right = solve(arr,k+1,j)

        temp = left+right+(arr[i-1]*arr[k]*arr[j])
        minimum = min(minimum,temp)


    m[i][j] = minimum
    return m[i][j]

if __name__ == '__main__':

    # Calling the function
    ans = solve(arr, 1, len(arr) - 1)

    # Print the min cost we need to multiply all the matrices
    print(ans)
