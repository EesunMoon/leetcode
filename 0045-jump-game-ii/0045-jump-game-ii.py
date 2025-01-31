class Solution:
    def jump(self, nums: List[int]) -> int:
        # DP : variable index state the numbere of jumps
        # T O(n*m) S O(n)
        dp = [float("INF")] * (len(nums))
        dp[len(nums)-1] = 0 # goal

        for i in range(len(nums)-2, -1, -1):
            for j in range(nums[i], 0, -1):
                if i + j >= len(nums):
                    dp[i] = 1
                    break
                dp[i] = min(dp[i], 1 + dp[i+j])
        return dp[0]