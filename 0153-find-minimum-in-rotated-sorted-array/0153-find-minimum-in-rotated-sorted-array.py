class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        smallest = nums[l]
        
        while l<=r:
            # sorted
            if nums[l] < nums[r]:
                smallest = min(smallest, nums[l])
                break
                
            m = (l+r)//2
            smallest = min(smallest, nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        
        return smallest

        