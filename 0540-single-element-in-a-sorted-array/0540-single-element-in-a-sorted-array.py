class Solution(object):

    def partition(self, nums, start, end):
        median = (start+end)//2
        # print(nums, start, end)
        if median-start == 1:
            if nums[start] != nums[median]:
                return nums[start]
            if nums[median] != nums[end]:
                return nums[end]
        
        if nums[median-1] != nums[median] and nums[median+1] != nums[median]:
            return nums[median]
        if (end-start+1)//2 % 2 == 0:
            if nums[median -1] == nums[median]:
                return self.partition(nums, start, median)
            else:
                return self.partition(nums, median, end)
        else:
            if nums[median -1] == nums[median]:
                return self.partition(nums, median-1, end)
            else:
                return self.partition(nums, start, median+1)


    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach
        # if median-1 == median then left
        # if median+1 == median then right

        # Base Case
        if len(nums) == 1:
            return nums[0]

        return self.partition(nums, 0, len(nums)-1)
        