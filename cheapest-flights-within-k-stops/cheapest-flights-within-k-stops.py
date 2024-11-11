class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # initialize DP
        dp = [float("inf")]*n
        dp[src] = 0
        
        for i in range(k+1):
            temp = dp[:]
            for start, end, weight in flights:
                if dp[start] != float("inf"):
                    # recurrence relation
                    temp[end] = min(temp[end], dp[start]+weight)
            dp = temp
        
        return dp[dst] if dp[dst] != float("inf") else -1