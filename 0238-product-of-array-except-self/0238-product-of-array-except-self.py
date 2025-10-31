class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        prefix = 1
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        
        prefix = 1 # suffix
        for i in range(len(nums)-1, -1, -1):
            res[i] *= prefix
            prefix *= nums[i]
        return res