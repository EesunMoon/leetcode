class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # DP T O(n^3) S O(n^2)
        nums = [1] + nums + [1]

        dp = {} # (l, r)
        def dfs(l, r):
            # base case
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]
            
            # compute dp
            # recurrence relation: nums[L-1]*nums[i]*nums[R+1] + DP[i+1][R] + DP[L][i-1]
            dp[(l, r)] = 0
            for i in range(l, r+1):
                coins = nums[l-1]*nums[i]*nums[r+1]
                coins += (dfs(l, i-1) + dfs(i+1, r))
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
            
        return dfs(1, len(nums)-2) # original range