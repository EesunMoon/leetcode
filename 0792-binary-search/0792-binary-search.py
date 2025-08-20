class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target: # right boundary
                l = m + 1
            else: # left boundary
                r = m - 1
        return -1