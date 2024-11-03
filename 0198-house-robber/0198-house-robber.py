class Solution(object):
    def rob(self, nums):
        
        # [DP] State Variables: index
        #      Return: Maximum
        def dp(idx):
            # Base case
            if idx == 0:
                return nums[0]
            elif idx == 1:
                return max(nums[0], nums[1])
            
            # Recurrence Relation
            if idx not in cache:
                cache[idx] = max(dp(idx-1), dp(idx-2) + nums[idx])
            return cache[idx]

        # memoization
        cache = {}
        return dp(len(nums)-1) # refer to house index
        