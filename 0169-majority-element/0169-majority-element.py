class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = list(set(nums))
        k=0
        val=nums[0]
        for unique in nums_set:
            if nums.count(unique) > k:
                k=nums.count(unique)
                val=unique
                
        return val