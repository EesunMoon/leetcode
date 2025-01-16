class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        curMax, curMin = 1, 1

        for num in nums:
            if num == 0:
                curMax, curMin = 1, 1
                continue
            
            tmp = curMax*num
            curMax = max(curMax*num, curMin*num, num)
            curMin = min(tmp, curMin*num, num)
            res = max(res, curMax)
        return res