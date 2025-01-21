class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # DP solution
        # T O(m*n), S O(m*n)
        dp = [0] * (amount+1)
        dp[0] = 1 # 0 amount -> 1 way

        for i in range(len(coins)-1, -1, -1):
            newDP = [0] * (amount+1)
            newDP[0] = 1
            for a in range(amount+1):
                newDP[a] = dp[a]
                if a - coins[i] >= 0:
                    newDP[a] += newDP[a-coins[i]] # contain prior coin
            dp = newDP
        return dp[amount]
        """
        # caching
        # T O(m*n), S O(m*n)
        dp = {}
        def dfs(i, total):
            if total == amount:
                return 1
            if i >= len(coins) or total > amount:
                return 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i,total)] = dfs(i, total + coins[i]) + dfs(i+1, total)
            return dp[(i, total)]
        
        return dfs(0,0)
        """