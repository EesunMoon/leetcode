class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ## DP bottom up TC O(n*m) SC O(m) n: len(coins) m: amount
        # only use prior dp and current dp
        dp = [0] * (amount+1) # dp[amount] = count
        dp[0] = 1 # base case

        for i in range(len(coins)-1, -1, -1):
            currDP = [0] * (amount+1)
            currDP[0] = 1
            for a in range(1, amount+1):
                currDP[a] = dp[a]
                if a - coins[i] >= 0:
                    currDP[a] += currDP[a-coins[i]]
            dp = currDP
        return dp[amount]