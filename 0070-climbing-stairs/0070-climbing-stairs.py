class Solution:
    def climbStairs(self, n: int) -> int:
        # dp: variable step, state: #. of distinct way
        first, second = 1, 1 # i-1, i-2

        for i in range(2, n+1):
            tmp = first + second
            second = first
            first = tmp

        return first
    """
    def climbStairs(self, n: int) -> int:
        # dp: variable step, state: #. of distinct way
        dp = [float("INF")] * (1+n)
        
        # base case
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]


        return dp[n]
    """