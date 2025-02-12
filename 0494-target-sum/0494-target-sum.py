class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} #(index, amount): the number of expressions
        def dfs(i, total):
            # base case
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = dfs(i+1, total + nums[i]) + dfs(i+1, total - nums[i])
            return dp[(i, total)]
        return dfs(0, 0)
