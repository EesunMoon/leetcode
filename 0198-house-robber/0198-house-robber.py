class Solution:
    def rob(self, nums: List[int]) -> int:
        # Brute Force O(2^n) - 2 decision(contain or not)

        # DP - bottom up T O(n), S O(n)
        """
        DP = [0] * len(nums) # variable: house idx, state: maximum profit so far
        # base case
        DP[0], DP[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # recurrence relationship dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            DP[i] = max(nums[i]+DP[i-2], DP[i-1])
        return DP[len(nums)-1]
        """

        # optimal DP - T O(n), S O(1)
        if len(nums) == 1:
            return nums[0]
        # base case
        one, two = nums[0], max(nums[0], nums[1]) # DP[0], DP[1]

        for i in range(2, len(nums)):
            # recurrence relationship dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            tmp = max(nums[i]+one, two)
            one = two
            two = tmp
        return two