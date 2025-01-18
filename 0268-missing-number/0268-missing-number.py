class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        maxNum = len(nums)

        for i in range(maxNum+1):
            total += i
        
        return total - sum(nums)