class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        smallest = nums[0]

        while l<=r:
            # already sorted
            if nums[l] < nums[r]:
                smallest = min(smallest, nums[l])
                break
            
            # not sorted
            m = (l+r)//2
            smallest = min(smallest, nums[m])
            if nums[l] <= nums[m]:
                # m is in the left side => check right
                l = m+1
            else:
                # m is in the right side => check left
                r = m-1
        return smallest

        