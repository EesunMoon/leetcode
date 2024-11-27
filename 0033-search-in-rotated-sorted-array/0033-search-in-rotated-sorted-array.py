class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1

        # binary search => O(logn)
        while l<=r: 
            m = (l+r)//2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]: # left
                if nums[m] > target and target >= nums[l]:
                    r = m-1
                else:
                    l = m+1
            else: # right
                if nums[m] < target and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
                
        return -1
        