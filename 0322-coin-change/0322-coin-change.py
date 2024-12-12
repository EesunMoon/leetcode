class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # DSA: DP
        # idx: amount
        # states: #. of coins - minimum
        # recurrence relation: dp[i] = min(dp[i], 1+dp[amo - coin])

        dp = [float("inf")] * (amount+1) # bc dp[0] = 0
        dp[0] = 0 # base case

        for amo in range(1, amount+1):
            for coin in coins:
                if amo - coin >= 0:
                    dp[amo] = min(dp[amo], 1+dp[amo-coin])
        return dp[amount] if dp[amount] != float("inf") else -1
        
        