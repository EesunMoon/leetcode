class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subSum, maxSub = 0, nums[0]
        for num in nums:
            if subSum < 0:
                subSum = 0
            subSum += num
            maxSub = max(maxSub, subSum)
        return maxSub