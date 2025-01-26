"""
    Given an array arr[] of size n, 
    the task is to divide it into two sets S1 and S2 
    such that the absolute difference between their sums is minimum. 
    
    If there is a set S with n elements, 
    then if we assume Subset1 has m elements, 
    Subset2 must have n-m elements 
    and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.
"""

def solution(arr):
    # DP: state - avaiable or not, index: subsum
    total = sum(arr)
    dp = [False] * (total + 1)
    
    # base case: if subsum 0:: True
    dp[0] = True

    ## recurrence relation
    # if arr[i-1] > j: dp[i][j] = dp[i-1][j]
    # else: dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

    for num in arr:
        for subsum in range(total, num-1, -1):
            # recurrence relation
            dp[subsum] = dp[subsum] or dp[subsum - num]
    
    # calculate difference between subtotal
    res = total
    for subsum in range(total // 2 + 1):
        if dp[subsum]:
            res = min(res, abs(subsum - (total - subsum)))

    return res

# example
# arr = [1, 1, 9]
arr = [1, 2, 3, 4, 5]
print(solution(arr))
