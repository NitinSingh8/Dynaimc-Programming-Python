# Given the input arr and target
# What you can do :-
#                   You have to put '+' or '-' sign in front of every number in array/list
# Return -  the total number of ways you can form to subset that their sum will be equal to target

def find_zero(num):
    return len([x for x in num if x == 0])


def find_no_of_subset_sum(nums, s):
    n = len(nums)
    m = [[0] * (s + 1) for _ in range(n + 1)]

    m[0][0] = 1
    for i in range(n + 1):
        for j in range(s + 1):
            if i == 0 or j == 0:
                if i == 0:
                    m[i][j] = 0
                if j == 0:
                    m[i][j] = 2 ** find_zero(nums[:i])
        # print(s)
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if nums[i - 1] <= j:
                m[i][j] = m[i - 1][j] + m[i - 1][j - nums[i - 1]]
            else:
                m[i][j] = m[i - 1][j]

    return m[n][s]


def target_sum(nums, target):
    sum1 = (sum(nums) + target) // 2

    return find_no_of_subset_sum(nums, sum1)


# input
nums = [0, 0, 0, 0, 0, 0, 0, 0, 1]
target = 1

count = target_sum(nums, target)  # calling the function

print(count)  # print the number of ways
