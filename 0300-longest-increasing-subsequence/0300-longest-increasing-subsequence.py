class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp state: length of the longest way in index
        # dp index: index
        # bottomUp: dp[i] = 1 + max(dp[i+k]), k: n-1 ~ i+1, if num[i+k] > num[i]

        n = len(nums)
        dp = [1] * n
        for i in range(n-2, -1, -1):
            for k in range(n-1, i, -1):
                if nums[i] < nums[k]:
                    dp[i] = max(dp[i], 1 + dp[k])
        return max(dp[i] for i in range(n))