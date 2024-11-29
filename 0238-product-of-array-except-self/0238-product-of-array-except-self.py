class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # ex) 1, 2, 3, 4
        # 2*3*4, 1*3*4, 1*2*3
        # prefix 1, 1*1, 1*1*2, 1*1*3
        # suffix 1*4*3*2, 1*4*3,1*4,1
        # prefix * suffix
        # prefix start = 1
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result