class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp variable = position(index), state: #.of way
        
        dp = [1] * n
        # recurrent relation: dp[r+1][c] + dp[r][c+1]
        for r in range(m-2, -1, -1):
            newDP = [0] * (n+1)
            for c in range(n-1, -1, -1):
                newDP[c] = dp[c] + newDP[c+1]
            dp = newDP
        return dp[0]