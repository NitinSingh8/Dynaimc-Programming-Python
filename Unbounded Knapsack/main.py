# Unbounded Knapsack Problem.



def unbounded_knapsack(wt,val,w):
    n = len(wt)
    m = [[0]*(w+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            if wt[i-1]<=j:
                m[i][j] = max(val[i-1] + m[i][j-wt[i-1]] , m[i-1][j])
            else:
                m[i][j] =  m[i-1][j]
    return m[n][w]

# Input
weight = [1,3,4,5]
value = [1,4,5,7]
W = 7

maximum_profit = unbounded_knapsack(weight,value,W)

print(maximum_profit)