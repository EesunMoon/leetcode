class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1

        while l<=r:
            m = (l+r)//2

            if nums[m] == target:
                return m

            # left part
            if nums[l] <= nums[m]:
                if target > nums[m]:
                    l = m + 1
                elif target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # right part
            else:
                if target < nums[m]:
                    r = m-1
                elif target > nums[r]:
                    r = m-1
                else:
                    l = m+1

        return -1