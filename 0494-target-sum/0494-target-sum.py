class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = defaultdict(int)
        # base case
        dp[0] = 1 # sum 0 -> 1 way

        for i in range(len(nums)):
            newDP = defaultdict(int)
            for currSum, count in dp.items():
                newDP[currSum + nums[i]] += count
                newDP[currSum - nums[i]] += count
            dp = newDP
        return dp[target]