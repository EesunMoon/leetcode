class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # brute force: m**n, m = amount, n = len(coins)
        # [dp] T O(m*n) S O(m)
        # state: minimum number of coins, variable: amount
        dp = [float("INF")] * (amount+1)
        
        # base case
        dp[0] = 0 # 0 coin use

        for a in range(1, amount+1):
            for c in coins:
                if a-c >=0:
                    dp[a] = min(dp[a], dp[a-c]+1)
        
        return dp[amount] if dp[amount] != float("INF") else -1