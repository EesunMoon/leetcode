class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # caching
        dp = {} # (i, amount): count
        def dfs(i, amount):
            if i == len(nums):
                return 1 if amount == target else 0
            
            if (i, amount) in dp:
                return dp[(i,amount)]
            dp[(i, amount)] = dfs(i+1, amount + nums[i]) + dfs(i+1, amount - nums[i])
            return dp[(i, amount)]
        return dfs(0, 0)