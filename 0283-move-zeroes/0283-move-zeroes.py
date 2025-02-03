class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 0, 1, 0, 3, 12
        # 1, 1, 0, 0, 3

        l, r = 0, 0 # l: find index of 0, r: find index of not 0
        # find first index of 0
        while l < len(nums) and nums[l] != 0:
            l += 1
        r = l + 1
        while r < len(nums):
            while r < len(nums) and nums[r] == 0:
                r += 1
            if r == len(nums):
                break
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
        return nums