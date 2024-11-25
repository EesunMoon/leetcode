class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sorted in ascending order: binary search
        l, r = 0, len(nums)-1

        while l<=r:
            mid = l + ((r-l)//2)

            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                return mid
        return -1