class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        l = 0
        for r in range(len(nums)):
            while l<=r and nums[l] != 0:
                l += 1
            if nums[r] and l < r:
                nums[r], nums[l] = nums[l], nums[r]
        