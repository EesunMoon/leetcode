class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            newRob = max(num + rob1, rob2) # skip rob2
            rob1 = rob2
            rob2 = newRob
        return rob2 # obtain maximum value