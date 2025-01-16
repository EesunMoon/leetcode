class Solution(object):
    def minCostClimbingStairs(self, cost):
        N = len(cost)
        dp = [float("INF")] * (N+1)
        dp[N], dp[N-1] = 0, cost[N-1]

        for i in range(N-2, -1, -1):
            dp[i] = min(cost[i]+dp[i+1], cost[i] + dp[i+2])
        
        return min(dp[0], dp[1])
    # def minCostClimbingStairs(self, cost):
        # """
        # :type cost: List[int]
        # :rtype: int
        # """
        # def dp(idx):
        #     # base case
        #     if idx == 0 or idx == 1:
        #         return 0
            
        #     if idx not in cache:
        #         cache[idx] = min(dp(idx-1)+cost[idx-1], dp(idx-2)+cost[idx-2])
        #     return cache[idx]
        

        # cache = {}
        # return dp(len(cost))