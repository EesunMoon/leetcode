class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # counting sort
        counts = [0] * (2+1)
        for num in nums:
            counts[num] += 1
        start = 0
        for i, cnt in enumerate(counts):
            counts[i] = start
            start += cnt
        
        sorted_nums = [0] * len(nums)
        for num in nums:
            sorted_nums[counts[num]] = num
            counts[num] += 1
        
        for i in range(len(nums)):
            nums[i] = sorted_nums[i]
        return nums
