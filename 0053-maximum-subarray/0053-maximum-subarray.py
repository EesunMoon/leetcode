class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force O(n^2) => for all subarray
        # [-2,1,-3,4,-1,2,1,-5,4]
        # subSum < 0
        # [-2, -1, -2, -1, -2, -1, -2, -1]
        # sliding window

        l = 0
        subSum = 0
        maxNum = nums[0]
        for r in range(len(nums)):
            subSum += nums[r]
            maxNum = max(subSum, maxNum)
            if subSum < nums[r]:
                maxNum = max(maxNum, nums[r])
                l = r
                subSum = nums[r]
        return maxNum