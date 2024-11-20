class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        counts = {}

        for idx, num in enumerate(nums):
            counts[num] = idx
        
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in counts and counts[diff] != idx:
                return [idx, counts[diff]]

        return []
        